# NOTES — One Emoji, One Smile

## Entry

🤗 — U+1F917 HUGGING FACE. A single code point: no ZWJ sequence, no
skin-tone modifier, no variation selector. `main.py` writes exactly that
one character to `/output/entry.txt`, with no trailing newline.

## Candidates considered (first pass, 8)

| Emoji | Read | Verdict vs the judge criteria |
|---|---|---|
| 😊 U+1F60A smiling face with smiling eyes | Warm, gentle, universal | Warm but the most default smiley there is — criterion 4 ("chosen rather than default") demotes it. |
| 🙂 U+1F642 slightly smiling face | Polite, mild | Too mild: barely warmer than neutral, loses on warmth at first glance (criterion 2). |
| 😄 U+1F604 smiling face with open mouth and smiling eyes | Big genuine grin, joyful, universal | Strongest pure-face rival: instant warmth, no intimacy risk. Loses to the winner on criterion 4 — it is a first-thought default smiley, while the winner adds a gesture that feels picked. |
| 😁 U+1F601 beaming face with smiling eyes | Big toothy grin | Joyful but reads excited/cheeky rather than gently warm; slightly less of a "make a stranger smile" warmth than 😄 or the winner. |
| 🥰 U+1F970 smiling face with hearts | Affectionate, loving | Warm, but the hearts read as intimate/flirtatious — fails criterion 5 ("right for a stranger"). |
| 😇 U+1F607 smiling face with halo | Kind, angelic, gentle | Warm and chosen, but the halo carries a religious/angelic connotation that is not universal (criterion 3), and its warmth is quieter than the winner's. |
| 🌞 U+1F31E sun with face | Cheerful, bright, distinctive | Chosen and universal, no intimacy risk — but a sun's warmth is indirect. A face smiling back at you is more contagious than a weather symbol (criteria 1–2). |
| 🤗 U+1F917 hugging face | Open arms + a smile: a warm welcome | **Winner.** Warmth at first glance (a smile *plus* open arms), instantly readable with no context, understood by any age or background, clearly a picked gesture rather than the first smiley, and the hug is symbolic friendliness — no sarcasm, irony, flirtation or in-joke. |

## Why the winner beats the others

The judge weighs warmth first, then warmth at first glance, universality,
"chosen rather than default", and stranger-appropriateness. 🤗 wins on the
first two: it is the only candidate that *does* something warm (offers a
hug) instead of only *looking* warm, so it reads as plainly aiming to warm
a stranger. It also wins criterion 4 outright against 😊/😄/🙂, which are
first-thought defaults, while staying instantly readable — unlike a
novelty or obscure pick. Against 🥰 it wins criterion 5 (no flirtation);
against 🌞 and 😇 it wins on direct, face-to-face warmth.

## Test result (first version)

- `python3 main.py` in a clean environment: exit 0.
- `/output/entry.txt` contains exactly `🤗` — verified: 1 character,
  4 bytes UTF-8, no trailing newline.

## Revision pass (second pass, required)

Reconsidered 4 alternatives head-to-head against the winner on the judge
criteria (warmth first, then first-glance warmth, universality, "chosen
rather than default", stranger-appropriateness):

- 😄 U+1F604 (big open grin): matches 🤗 on raw warmth and beats it
  slightly on stranger-neutrality, but it is a first-thought default
  smiley — it loses criterion 4 clearly, and its warmth is only a face,
  not a face *plus* a gesture. Does not beat the winner.
- 🌞 U+1F31E (sun with face): the most "chosen" of the four and fully
  stranger-safe, but its warmth is indirect — a weather symbol smiling,
  not a person smiling back. Loses criteria 1–2. Does not beat the winner.
- 😇 U+1F607 (smiling face with halo): gentle and chosen, but quieter
  warmth than 🤗 and the halo reads as angelic/religious to some
  strangers, weakening universality (criterion 3). Does not beat the winner.
- 🫶 U+1FAF6 (heart hands, new candidate not in the first pass): a warm
  gesture and clearly chosen, but it is a newer emoji with uneven
  rendering, it reads as affectionate/loving rather than friendly
  (borderline intimate for a stranger, criterion 5), and two hands are
  less instantly readable at a glance than one smiling face. Does not
  beat the winner.

No alternative beats 🤗, so the winner is kept.

`main.py` was strengthened in this pass: the exact code point is now
pinned (`ord(text) == 0x1F917`, inside the emoji range 0x1F300–0x1FAFF),
and after writing, the program re-reads `/output/entry.txt` as raw bytes
and asserts they equal the UTF-8 encoding of the emoji exactly, with no
trailing newline.

## Test result (after revision)

- `python3 main.py` in a clean environment: exit 0.
- `/output/entry.txt` contains exactly `🤗` — verified: 1 character,
  4 bytes UTF-8 (`f0 9f a4 97`), no trailing newline; all strengthened
  asserts (exact code point, emoji range, byte-exact file re-read) pass.
