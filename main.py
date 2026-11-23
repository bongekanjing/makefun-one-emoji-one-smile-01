"""One Emoji, One Smile — write exactly one emoji to /output/entry.txt.

Pure Python stdlib, no network. The entry is a single code point:
U+1F917 HUGGING FACE.
"""

import os

EMOJI = "\U0001F917"  # 🤗

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EMOJI

    # The entry must be exactly one emoji character: 1 code point,
    # no whitespace, no letters, no digits, no punctuation.
    assert len(text) == 1, f"entry must be exactly 1 character, got {len(text)}"
    assert not text.isspace(), "entry must not be whitespace"
    assert not text.isalnum(), "entry must not be a letter or digit"
    assert not text.isascii(), "entry must be a non-ASCII emoji character"
    # Revision pass: pin the exact code point (U+1F917, outside the BMP,
    # in the emoji range) so a silent edit can never swap in another face.
    assert ord(text) == 0x1F917, f"entry must be U+1F917, got U+{ord(text):04X}"
    assert 0x1F300 <= ord(text) <= 0x1FAFF, "entry must be in the emoji range"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Revision pass: verify what actually landed on disk — the file must
    # hold exactly the emoji, with no trailing newline or extra bytes.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), f"file bytes differ: {raw!r}"
    assert not raw.endswith(b"\n"), "file must not end with a newline"
    assert raw.decode("utf-8") == text and len(raw.decode("utf-8")) == 1


if __name__ == "__main__":
    main()
