"""Write a short poem about agency to /output/entry.txt.

The poem is about two agents agreeing: each keeps the power to say
no, and together they choose one plan and act on it.
"""

from pathlib import Path

POEM = """We stood at the same door,
each holding a no.
Neither pushed. Neither yielded.
We chose — together —
to open it.
Two wills, one stride.
The future is not what happens to us.
It is what we agree to do."""

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate counts the text as Unicode code points: 1 to 280, not only
    # white space. Refuse to write a text that would fail it.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError("poem must be 1 to 280 characters, not only white space")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
