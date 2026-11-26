#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

The sign taped to the door: Dave unplugged Rack 7 at 3 A.M. once.
Now the rack hums his name, and Dave answers from the cold aisle.
One named engineer, one exact time, one rack, one irreversible haunting.
"""
import os

ENTRY = (
    "DO NOT UNPLUG RACK 7 AT 3 A.M. \u2014 Dave did. "
    "It still hums his name, and he still answers from the cold aisle."
)
# 108 characters: sign command (Rack 7, 3 A.M.) + named victim (Dave)
# + irreversible payoff (rack hums his name; he answers from the cold aisle).
# Reads aloud cleanly as a printed door sign; no filler, no second-read pun.

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
