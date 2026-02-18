#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from urllib.parse import urlparse

DELAYS: tuple[str, ...] = ("1d", "3d", "21d")


def validate_url(url: str) -> str:
    """Return *url* if it has scheme + netloc, else raise."""
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        raise argparse.ArgumentTypeError(f"invalid URL: {url}")
    return url


def schedule_notification(url: str, delay: str) -> list[str]:
    """Build the systemd-run command for a single delay."""
    return [
        "systemd-run",
        "--user",
        f"--on-active={delay}",
        "--",
        "notify-send",
        "Reminder",
        url,
    ]


def schedule_all(url: str, delays: tuple[str, ...] = DELAYS) -> None:
    """Schedule a notify-send for every delay in *delays*."""
    for delay in delays:
        cmd = schedule_notification(url, delay)
        subprocess.run(cmd, check=True)
        print(f"scheduled +{delay}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Schedule spaced-repetition reminders")
    parser.add_argument("url", type=validate_url)
    args = parser.parse_args()

    schedule_all(args.url)


if __name__ == "__main__":
    main()
