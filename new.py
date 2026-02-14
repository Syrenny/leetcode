#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[0]
SOLUTIONS_DIR = ROOT / "src" / "solutions"
TESTS_DIR = ROOT / "tests"


# ---------- utils ----------


def extract_slug(url: str) -> str:
    """Extract problem slug from LeetCode URL."""
    path = urlparse(url).path
    match = re.search(r"/problems/([^/]+)/?", path)
    if not match:
        raise ValueError("Could not extract slug from URL")
    return match.group(1)


def kebab_to_snake(value: str) -> str:
    """Convert kebab-case (and any non-alnum) to snake_case."""
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def solution_template(url: str, slug: str) -> str:
    """Python solution skeleton."""
    return f'''

class Solution:
    """LeetCode problem

    Link:
        {url}
    """

    def solve(self) -> None:
        raise NotImplementedError
'''


def test_template(import_path: str) -> str:
    """Pytest skeleton with NaiveSolution."""
    return f'''from {import_path} import Solution
import pytest

class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True
    
@pytest.mark.parametrize(
    ("x", "expected"),
    [
        (123, 321),
    ],
)
def test_simple(x: int, expected: int) -> None:
    solution = Solution()
    assert solution.reverse(x) == expected
'''


# ---------- main logic ----------


def create_files(url: str, pattern: str) -> tuple[Path, Path]:
    pattern = kebab_to_snake(pattern)

    raw_slug = extract_slug(url)
    slug = kebab_to_snake(raw_slug)

    filename = f"{slug}.py"

    sol_dir = SOLUTIONS_DIR / pattern
    sol_dir.mkdir(parents=True, exist_ok=True)

    sol_path = sol_dir / filename
    test_path = TESTS_DIR / f"test_{slug}.py"

    if sol_path.exists():
        raise FileExistsError(sol_path)
    if test_path.exists():
        raise FileExistsError(test_path)

    import_path = f"src.solutions.{pattern}.{slug}"

    sol_path.write_text(solution_template(url, slug), encoding="utf-8")
    test_path.write_text(test_template(import_path), encoding="utf-8")

    return sol_path, test_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--pattern", default="misc")
    args = parser.parse_args()

    sol, test = create_files(args.url, args.pattern)

    print(f"Created: {sol}")
    print(f"Created: {test}")


if __name__ == "__main__":
    main()
