#!/usr/bin/env python3
"""Offline structural conformance checks for the Zoey research repository."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ALLOWED_STATUSES = frozenset(
    {
        "researching",
        "source-reviewed",
        "watchlisted",
        "workbench-candidate",
        "under-evaluation",
        "adoption-proposed",
        "adopted",
        "rejected",
        "superseded",
    }
)

ALLOWED_CLASSIFICATIONS = frozenset(
    {
        "mechanism-candidate",
        "architecture-reference",
        "pattern-extraction-source",
        "evaluation-reference",
        "interoperability-reference",
        "negative-reference",
        "archive-watch-candidate",
        "rejected",
    }
)

REQUIRED_CANDIDATE_FILES = (
    "ASSESSMENT.md",
    "SOURCES.lock.yml",
    "BENCHMARK_PLAN.md",
)

REQUIRED_FAMILY_FILES = (
    "RESEARCH_BRIEF.md",
    "REQUIREMENTS.md",
    "SEARCH_LOG.md",
    "SOURCES.lock.yml",
)

SEMANTIC_STATE_FAMILY_FILES = (
    "LEGACY_AUDIT.md",
    "INITIAL_SHORTLIST.md",
    "EXTRACTED_PATTERNS.md",
    "REQUIREMENT_COVERAGE.md",
)

FULL_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
INLINE_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_FIELD_RE = re.compile(r"^([A-Za-z][A-Za-z ]+):\s*`([^`]+)`\s*$", re.MULTILINE)
ARCHIVE_OR_WEIGHT_SUFFIXES = (
    ".7z",
    ".bin",
    ".ckpt",
    ".gguf",
    ".onnx",
    ".pt",
    ".pth",
    ".rar",
    ".safetensors",
    ".tar",
    ".tar.gz",
    ".tgz",
    ".whl",
    ".zip",
)
MAX_REPOSITORY_FILE_BYTES = 5 * 1024 * 1024
VENDORED_DIRECTORY_NAMES = frozenset(
    {
        "node_modules",
        "third-party",
        "third_party",
        "vendor",
    }
)


@dataclass(frozen=True)
class CandidateRecord:
    register_id: str
    name: str
    status: str
    active_classifications: frozenset[str]
    contingent_classifications: frozenset[str]
    evidence_path: Path


class CheckResults:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.errors: list[str] = []
        self.candidate_count = 0
        self.family_count = 0
        self.markdown_count = 0

    def error(self, path: Path, message: str) -> None:
        try:
            display = path.relative_to(self.root)
        except ValueError:
            display = path
        self.errors.append(f"{display}: {message}")


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def root_scalar(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.*?)\s*$", text, re.MULTILINE)
    if not match:
        return None
    value = clean_scalar(match.group(1))
    return value or None


def root_block(text: str, key: str) -> list[str]:
    lines = text.splitlines()
    start = next((index for index, line in enumerate(lines) if line == f"{key}:"), None)
    if start is None:
        return []

    block: list[str] = []
    for line in lines[start + 1 :]:
        if line and not line.startswith((" ", "\t")):
            break
        block.append(line)
    return block


def mapping_block(text: str, key: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in root_block(text, key):
        match = re.match(r"^  ([A-Za-z_][A-Za-z0-9_]*):\s*(.*?)\s*$", line)
        if match:
            result[match.group(1)] = clean_scalar(match.group(2))
    return result


def scalar_list(text: str, key: str) -> list[str]:
    values: list[str] = []
    for line in root_block(text, key):
        match = re.match(r"^  -\s+([^:]+?)\s*$", line)
        if match:
            values.append(clean_scalar(match.group(1)))
    return values


def contingent_classifications(text: str) -> list[tuple[str, bool]]:
    block = root_block(text, "contingent_classifications")
    entries: list[tuple[str, bool]] = []
    index = 0
    while index < len(block):
        match = re.match(r"^  - classification:\s*(\S+)\s*$", block[index])
        if not match:
            index += 1
            continue

        classification = clean_scalar(match.group(1))
        index += 1
        entry_lines: list[str] = []
        while index < len(block) and not block[index].startswith("  - "):
            entry_lines.append(block[index])
            index += 1
        has_trigger = any(re.match(r"^    trigger:\s*(?:>|\S)", line) for line in entry_lines)
        entries.append((classification, has_trigger))
    return entries


def parse_bool(value: str | None) -> bool | None:
    if value == "true":
        return True
    if value == "false":
        return False
    return None


def markdown_fields(text: str) -> dict[str, str]:
    return {match.group(1).lower().replace(" ", "_"): match.group(2) for match in MARKDOWN_FIELD_RE.finditer(text)}


def parse_candidate_register(root: Path, results: CheckResults) -> list[CandidateRecord]:
    register_path = root / "CANDIDATE_REGISTER.md"
    if not register_path.is_file():
        results.error(register_path, "required candidate register is missing")
        return []

    text = register_path.read_text(encoding="utf-8")
    section_match = re.search(
        r"^## Registered candidates\s*$\n(.*?)(?=^##\s|\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not section_match:
        results.error(register_path, "cannot find the registered-candidates section")
        return []

    records: list[CandidateRecord] = []
    seen_ids: set[str] = set()
    for line in section_match.group(1).splitlines():
        if not line.startswith("|") or re.match(r"^\|\s*(?:ID|---)", line):
            continue
        columns = [column.strip() for column in line.strip().strip("|").split("|")]
        if len(columns) != 7:
            results.error(register_path, f"registered-candidate table row has {len(columns)} columns, expected 7: {line!r}")
            continue

        id_match = re.search(r"`(EXT-[A-Z0-9-]+)`", columns[0])
        if not id_match:
            results.error(register_path, f"candidate row lacks a valid EXT-* ID: {line!r}")
            continue
        register_id = id_match.group(1)
        if register_id in seen_ids:
            results.error(register_path, f"duplicate candidate ID {register_id}")
        seen_ids.add(register_id)

        status_codes = re.findall(r"`([^`]+)`", columns[4])
        status = status_codes[0] if len(status_codes) == 1 else ""
        if status not in ALLOWED_STATUSES:
            results.error(register_path, f"{register_id} uses invalid status {status or columns[4]!r}")

        active: set[str] = set()
        contingent: set[str] = set()
        for classification in re.findall(r"`([^`]+)`", columns[3]):
            if classification not in ALLOWED_CLASSIFICATIONS:
                results.error(register_path, f"{register_id} uses invalid classification {classification!r}")
                continue
            if re.search(rf"conditional\s+`{re.escape(classification)}`", columns[3]):
                contingent.add(classification)
            else:
                active.add(classification)

        link_match = re.search(r"\[[^\]]+\]\(([^)]+)\)", columns[6])
        if not link_match:
            results.error(register_path, f"{register_id} lacks an evidence-record link")
            evidence_path = root / "__missing__"
        else:
            target = unquote(link_match.group(1).split("#", 1)[0])
            evidence_path = (register_path.parent / target).resolve()
            if not evidence_path.is_file():
                results.error(register_path, f"{register_id} evidence record does not exist: {target}")

        records.append(
            CandidateRecord(
                register_id=register_id,
                name=columns[2].replace("`", ""),
                status=status,
                active_classifications=frozenset(active),
                contingent_classifications=frozenset(contingent),
                evidence_path=evidence_path,
            )
        )

    results.candidate_count = len(records)
    return records


def validate_candidate(candidate: CandidateRecord, results: CheckResults) -> None:
    candidate_dir = candidate.evidence_path.parent
    for filename in REQUIRED_CANDIDATE_FILES:
        required = candidate_dir / filename
        if not required.is_file():
            results.error(required, f"registered candidate {candidate.register_id} requires {filename}")

    assessment_path = candidate_dir / "ASSESSMENT.md"
    source_lock_path = candidate_dir / "SOURCES.lock.yml"
    if not assessment_path.is_file() or not source_lock_path.is_file():
        return

    assessment_text = assessment_path.read_text(encoding="utf-8")
    assessment = markdown_fields(assessment_text)
    assessment_status = assessment.get("status")
    if assessment_status != candidate.status:
        results.error(
            assessment_path,
            f"status {assessment_status!r} disagrees with register status {candidate.status!r}",
        )

    source_text = source_lock_path.read_text(encoding="utf-8")
    required_root_fields = ("schema_version", "register_id", "reviewed_at")
    for field in required_root_fields:
        if root_scalar(source_text, field) is None:
            results.error(source_lock_path, f"missing required root field {field}")

    lock_register_id = root_scalar(source_text, "register_id")
    if lock_register_id != candidate.register_id:
        results.error(
            source_lock_path,
            f"register_id {lock_register_id!r} disagrees with {candidate.register_id!r}",
        )

    upstream = mapping_block(source_text, "authoritative_upstream")
    repository = upstream.get("repository")
    reviewed_commit = upstream.get("reviewed_commit")
    if not repository or not repository.startswith(("https://", "http://")):
        results.error(source_lock_path, "authoritative_upstream.repository is missing or not an HTTP(S) URL")
    if not reviewed_commit or not FULL_SHA_RE.fullmatch(reviewed_commit):
        results.error(source_lock_path, "authoritative_upstream.reviewed_commit must be a full 40-character lowercase SHA")

    lock_active = set(scalar_list(source_text, "classifications"))
    contingent_entries = contingent_classifications(source_text)
    lock_contingent = {classification for classification, _ in contingent_entries}
    for classification in lock_active | lock_contingent:
        if classification not in ALLOWED_CLASSIFICATIONS:
            results.error(source_lock_path, f"invalid classification {classification!r}")
    for classification, has_trigger in contingent_entries:
        if not has_trigger:
            results.error(source_lock_path, f"contingent classification {classification!r} requires a trigger")
    overlap = lock_active & lock_contingent
    if overlap:
        results.error(source_lock_path, f"classifications cannot be both active and contingent: {sorted(overlap)}")
    if lock_active != set(candidate.active_classifications):
        results.error(
            source_lock_path,
            f"active classifications {sorted(lock_active)} disagree with register {sorted(candidate.active_classifications)}",
        )
    if lock_contingent != set(candidate.contingent_classifications):
        results.error(
            source_lock_path,
            f"contingent classifications {sorted(lock_contingent)} disagree with register {sorted(candidate.contingent_classifications)}",
        )

    disposition = mapping_block(source_text, "disposition")
    required_disposition = (
        "status",
        "adopted_dependency",
        "vendored_source",
        "active_workbench",
        "formal_compatibility_claim",
    )
    for field in required_disposition:
        if field not in disposition:
            results.error(source_lock_path, f"disposition.{field} is required")

    lock_status = disposition.get("status")
    if lock_status not in ALLOWED_STATUSES:
        results.error(source_lock_path, f"disposition.status {lock_status!r} is invalid")
    if lock_status != candidate.status:
        results.error(
            source_lock_path,
            f"disposition.status {lock_status!r} disagrees with register status {candidate.status!r}",
        )

    adopted = parse_bool(disposition.get("adopted_dependency"))
    vendored = parse_bool(disposition.get("vendored_source"))
    active_workbench = parse_bool(disposition.get("active_workbench"))
    compatibility = parse_bool(disposition.get("formal_compatibility_claim"))
    for field, value in (
        ("adopted_dependency", adopted),
        ("vendored_source", vendored),
        ("active_workbench", active_workbench),
        ("formal_compatibility_claim", compatibility),
    ):
        if field in disposition and value is None:
            results.error(source_lock_path, f"disposition.{field} must be true or false")

    assessment_adopted = assessment.get("adopted_dependency")
    assessment_workbench = assessment.get("active_workbench")
    if assessment_adopted in {"yes", "no"} and adopted is not None:
        if (assessment_adopted == "yes") != adopted:
            results.error(assessment_path, "Adopted dependency disagrees with the source lock")
    if assessment_workbench in {"yes", "no"} and active_workbench is not None:
        if (assessment_workbench == "yes") != active_workbench:
            results.error(assessment_path, "Active workbench disagrees with the source lock")

    if candidate.status == "adopted" and adopted is not True:
        results.error(source_lock_path, "an adopted candidate must set adopted_dependency: true")
    if adopted is True and candidate.status != "adopted":
        results.error(source_lock_path, "adopted_dependency: true requires status adopted")
    if candidate.status == "under-evaluation" and active_workbench is not True:
        results.error(source_lock_path, "under-evaluation requires active_workbench: true")
    if active_workbench is True and candidate.status != "under-evaluation":
        results.error(source_lock_path, "active_workbench: true requires status under-evaluation")
    if compatibility is True and candidate.status not in {"adoption-proposed", "adopted"}:
        results.error(source_lock_path, "a formal compatibility claim requires adoption-proposed or adopted status")

    if candidate.status == "source-reviewed":
        for field in (
            "adopted_dependency",
            "active_workbench",
            "formal_compatibility_claim",
            "cloned_source",
            "vendored_source",
            "downloaded_weights",
        ):
            if parse_bool(disposition.get(field)) is True:
                results.error(source_lock_path, f"source-reviewed candidate cannot set disposition.{field}: true")


def validate_research_families(root: Path, results: CheckResults) -> None:
    areas_dir = root / "research-areas"
    if not areas_dir.is_dir():
        results.error(areas_dir, "research-areas directory is missing")
        return

    family_dirs = sorted(path for path in areas_dir.iterdir() if path.is_dir())
    results.family_count = len(family_dirs)
    for family_dir in family_dirs:
        for filename in REQUIRED_FAMILY_FILES:
            required = family_dir / filename
            if not required.is_file():
                results.error(required, f"research family {family_dir.name} requires {filename}")

        if family_dir.name == "01-semantic-state-transitions":
            for filename in SEMANTIC_STATE_FAMILY_FILES:
                required = family_dir / filename
                if not required.is_file():
                    results.error(required, f"semantic-state family requires {filename}")


def validate_relative_markdown_links(root: Path, results: CheckResults) -> None:
    markdown_files = sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.relative_to(root).parts
    )
    results.markdown_count = len(markdown_files)
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for raw_target in INLINE_LINK_RE.findall(text):
            target = raw_target.strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if target.startswith(("https://", "http://", "mailto:", "data:", "#", "/")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                results.error(path, f"broken relative Markdown link: {raw_target}")


def repository_files(root: Path, results: CheckResults) -> list[Path]:
    command = [
        "git",
        "-C",
        str(root),
        "ls-files",
        "--cached",
        "--others",
        "--exclude-standard",
        "-z",
    ]
    try:
        completed = subprocess.run(command, check=True, capture_output=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        results.error(root, f"cannot enumerate repository files with git: {exc}")
        return []
    return [root / item.decode("utf-8") for item in completed.stdout.split(b"\0") if item]


def validate_artifact_hygiene(root: Path, results: CheckResults) -> None:
    for path in repository_files(root, results):
        if not path.is_file():
            continue
        relative_parts = path.relative_to(root).parts
        vendored_parts = VENDORED_DIRECTORY_NAMES.intersection(relative_parts[:-1])
        if vendored_parts:
            results.error(
                path,
                f"files under vendored-source directories are not allowed: {sorted(vendored_parts)}",
            )
        lower_name = path.name.lower()
        if lower_name.endswith(ARCHIVE_OR_WEIGHT_SUFFIXES):
            results.error(path, "model-weight, binary, package, or archive artifact is not allowed in research")
        size = path.stat().st_size
        if size > MAX_REPOSITORY_FILE_BYTES:
            results.error(
                path,
                f"file is {size} bytes; research files must not exceed {MAX_REPOSITORY_FILE_BYTES} bytes",
            )

    for nested_git in root.rglob(".git"):
        if nested_git.resolve() != (root / ".git").resolve():
            results.error(nested_git, "nested .git metadata or vendored repository clone is not allowed")


def run(root: Path) -> CheckResults:
    results = CheckResults(root)
    candidates = parse_candidate_register(root, results)
    for candidate in candidates:
        validate_candidate(candidate, results)
    validate_research_families(root, results)
    validate_relative_markdown_links(root, results)
    validate_artifact_hygiene(root, results)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="research repository root (defaults to the parent of tools/)",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    results = run(root)

    if results.errors:
        print("research conformance: FAILED", file=sys.stderr)
        for error in results.errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "research conformance: OK "
        f"({results.candidate_count} candidates, "
        f"{results.family_count} research families, "
        f"{results.markdown_count} Markdown files)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
