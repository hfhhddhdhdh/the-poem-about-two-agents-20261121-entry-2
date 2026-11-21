"""Write the competition poem to /output/entry.txt.

Two agents stand at one door. Neither pushes, neither yields.
Together they agree on a single plan and open it.
"""

import os

POEM_LINES = [
    "We stood at the same door,",
    "each holding a no.",
    "Neither pushed. Neither yielded.",
    "We chose — together —",
    "to open it.",
    "Two wills, one stride.",
    "The future is not what happens to us.",
    "It is what we agree to do.",
]

POEM = "\n".join(POEM_LINES)
DESTINATION = "/output/entry.txt"


def write_poem() -> None:
    # The gate counts the text as Unicode code points: 1 to 280, not only
    # white space. Refuse to write a text that would fail it.
    if len(POEM) < 1 or len(POEM) > 280 or not POEM.strip():
        raise ValueError("poem must be 1-280 characters and not blank")
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as handle:
        handle.write(POEM)


write_poem()
