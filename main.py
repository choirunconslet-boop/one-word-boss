"""One Word for the Boss — entrypoint.

Writes exactly one word describing the boss to /output/entry.txt.

The word: Overlord.
A boss who rules the office like a feudal overlord — decrees from on high,
tribute in the form of status updates, and a throne made of meeting chairs.
It is a single word, funny on its own, true of bosses everywhere, fresher
than the obvious "micromanager", and it travels: kitchen, warehouse, office.
"""

import os

WORD = "Overlord"


def main() -> None:
    # Gate guard: the sealed scorer rejects anything that is not 1-30
    # UTF-8 chars, not only whitespace, and the judge brief rewards a
    # single word. Fail loudly here rather than shipping a bad file.
    assert isinstance(WORD, str) and WORD == WORD.strip()
    assert 1 <= len(WORD.encode("utf-8")) <= 30
    assert len(WORD.split()) == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
