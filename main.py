"""Funniest Time Machine Warning Label entry.

Writes a single one-line warning label for a time machine to
/output/entry.txt. The text must be plain ASCII, one line, 1-120
characters. The label keeps a straight official face while turning
the duplicate-self paradox into the joke, saving the twist for the
last few words.
"""

LABEL = "WARNING: If you meet yourself, do not wave. You will wave back, and then neither of you will ever leave."


def main():
    text = LABEL.strip()
    # Gate self-check: mirror the sealed scorer (1-120 chars, not only
    # whitespace, plain ASCII, a single line) so we never write an
    # invalid entry.
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
