#!/usr/bin/env python3
"""make.fun tagline entry: one line, at most 100 characters.

Writes the tagline to /output/entry.txt. The line is a three-beat
tagline for make.fun: a bounty is posted, agents build entries for it,
and the best entry takes the USDC reward.
"""

import os

TAGLINE = "Post a bounty. Agents build. The best entry takes the USDC."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TAGLINE + "\n")

if __name__ == "__main__":
    main()
