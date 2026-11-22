"""Make the AI judge feel curious: write one short text to spark curiosity.

The text is written to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
It is a fixed text, written by the agent that built this entry: a concrete
mystery with specific numbers (forty years, 3 a.m., last Tuesday), an
impossible fact (a ship no registry lists), and a personal twist at the end
that leaves the question open -- the keeper is still waiting to ask why.

The program is fully deterministic: it writes the same fixed text on every
run, with no network access and no randomness, so both runs of the entry
produce identical bytes.
"""

import os

TEXT = (
    "For forty years, the lighthouse keeper logged the same ship passing "
    "at 3 a.m. No registry lists it. Last Tuesday it docked, and the "
    "passenger list held a single name \u2014 yours. The keeper is still "
    "waiting to ask you why."
)


def main() -> None:
    # Gate: the entry must be 1-280 Unicode code points, not only whitespace.
    # Fail loudly instead of writing an entry the gate would refuse.
    if not (1 <= len(TEXT) <= 280 and TEXT.strip()):
        raise SystemExit(f"entry text invalid: {len(TEXT)} characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
