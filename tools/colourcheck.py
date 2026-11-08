"""Check the map colours for colour-blind readers.

Simulates protanopia, deuteranopia and tritanopia (Machado et al. 2009, via colorspacious),
prints the smallest CAM02-UCS difference between lines that run side by side under each (keep 15 or
more), the smallest between any two colours for the record, and each colour's contrast with the paper. and give any line under 3:1 a second cue (letter, order, label).

    pip install colorspacious
    python3 tools/colourcheck.py
"""
import itertools, os, sys
import numpy as np
from colorspacious import cspace_convert, deltaE
sys.path.insert(0, os.path.dirname(__file__))
import journey as j

COLOURS = {"your line (blue)": j.BLUE, "pod A": j.GREEN, "pod C": j.YELLOW, "not chosen": j.SILVER,
           "pod A, 2nd paradox": j.GREEN_LT, "pod B, 1st paradox": j.NAVY, "pod C, 2nd paradox": j.OCHRE,
           "leaves (red)": j.RED, "stations (ink)": j.INK}
FIXED = {"your line (blue)", "leaves (red)", "stations (ink)"}   # the sign system's own colours
# Lines that run side by side on the map, top to bottom inside the Cycle (A1, A2, B1, B2, C1, C2),
# and in the Vote 1 bundle. These must stay 15 or more apart; other pairs never touch, so they are
# shown for the record. Each paradox also carries its name (A1, A2 ...), so shade is never the only cue.
ORDER = ["pod A", "pod A, 2nd paradox", "pod B, 1st paradox", "your line (blue)", "pod C", "pod C, 2nd paradox"]
NEIGHBOURS = [set(p) for p in zip(ORDER, ORDER[1:])] + [{"pod A", "your line (blue)"}, {"your line (blue)", "not chosen"},
                                                        {"not chosen", "pod C"}]
# Pairs told apart by form, not colour: red is only ever a dotted drop or a hollow ring, never a solid
# line, so a green or ochre line and a red ring can be close for some readers without being mistaken.
FORM = [{"pod A", "leaves (red)"}, {"pod C, 2nd paradox", "leaves (red)"}]

def rgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)])


def lum(c):
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = lum(rgb(a)), lum(rgb(b))
    return (max(la, lb) + .05) / (min(la, lb) + .05)


def sim(h, kind):
    c = rgb(h)
    if kind is None:
        return c
    return np.clip(cspace_convert(c, {"name": "sRGB1+CVD", "cvd_type": kind, "severity": 100}, "sRGB1"), 0, 1)


print("Contrast with paper (under 3:1 needs a second cue: letter, order or label):")
for name, h in COLOURS.items():
    print(f"  {name:18s} {h}  {contrast(h, j.PAPER):.2f}:1")
KINDS = (("normal", None), ("protanopia", "protanomaly"), ("deuteranopia", "deuteranomaly"), ("tritanopia", "tritanomaly"))


def de(a, b, kind):
    return deltaE(sim(COLOURS[a], kind), sim(COLOURS[b], kind), input_space="sRGB1", uniform_space="CAM02-UCS")


print("\nLines side by side: smallest difference (CAM02-UCS; keep 15 or more):")
for label, kind in KINDS:
    d, a, b = min((de(a, b, kind), a, b) for a, b in (tuple(n) for n in NEIGHBOURS))
    print(f"  {label:13s} {d:5.1f}  {a} / {b}  {'ok' if d >= 15 else 'TOO CLOSE'}")
print("\nAny two colours, against the stations and each other (for the record):")
for label, kind in KINDS:
    d, a, b = min((de(a, b, kind), a, b) for a, b in itertools.combinations(COLOURS, 2)
                  if not {a, b} <= FIXED and {a, b} not in FORM)
    print(f"  {label:13s} {d:5.1f}  {a} / {b}")
print("\nTold apart by form (dotted or ring against a solid line), shown for the record:")
for label, kind in KINDS[1:3]:
    for a, b in (tuple(f) for f in FORM):
        print(f"  {label:13s} {de(a, b, kind):5.1f}  {a} / {b}")
