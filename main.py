"""One-line office joke entry for make.fun.

Writes a single joke about office life to entry.txt. The grader runs this
program with a read-only working directory, so the output goes to the
directory make.fun names first: $MAKEFUN_OUTPUT_DIR, then /output when it
exists, and only then a local output/ folder for a plain local run.
"""

import os

JOKE = (
    "I booked a meeting to cut down on meetings, and it ran so long "
    "we scheduled a follow-up about the follow-up."
)


def output_dir() -> str:
    """Pick where entry.txt goes, in the grader's preferred order."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "output")


def main() -> None:
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
