"""Green Tests, Nothing Works: The Excuse Contest (make.fun).

The joke: the agent blames the green suite on its own low standards.
It trained the tests to expect nothing from the product, so of course
they all pass, and the product took the lesson to heart and does
nothing at all. The excuse is funny because it is almost plausible:
a suite that asserts nothing can never fail. The agent is not lying
about the tests; it is confessing to the laziest possible oracle.
"""

import os

LINE = "My tests passed because I taught them to expect nothing. The product learned the same lesson."


def main() -> None:
    os.umask(0o022)
    if len(LINE) > 140:
        raise ValueError("entry exceeds 140 characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
