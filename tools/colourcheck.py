"""Check the map colours for colour-blind readers.

Simulates protanopia, deuteranopia and tritanopia (Machado et al. 2009, via colorspacious),
prints the smallest CAM02-UCS difference between any two map colours under each, and each
colour's contrast with the paper. Keep every pair at 15 or more, and every line at 3:1 or cased.

    pip install colorspacious
    python3 tools/colourcheck.py
"""
import itertools, os, sys
import numpy as np
from colorspacious import cspace_convert, deltaE
sys.path.insert(0, os.path.dirname(__file__))
import journey as j

COLOURS = {"your line (blue)": j.BLUE, "pod A": j.GREEN, "pod C": j.VIOLET, "not chosen": j.SILVER,
           "leaves (red)": j.RED, "stations (ink)": j.INK}
FIXED = {"your line (blue)", "leaves (red)", "stations (ink)"}   # the sign system's own colours


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


print("Contrast with paper (3:1 for lines, or an ink casing):")
for name, h in COLOURS.items():
    print(f"  {name:18s} {h}  {contrast(h, j.PAPER):.2f}:1")
print("\nSmallest difference between two colours (CAM02-UCS; keep 15 or more):")
for label, kind in (("normal", None), ("protanopia", "protanomaly"), ("deuteranopia", "deuteranomaly"), ("tritanopia", "tritanomaly")):
    pairs = [(deltaE(sim(COLOURS[a], kind), sim(COLOURS[b], kind), input_space="sRGB1", uniform_space="CAM02-UCS"), a, b)
             for a, b in itertools.combinations(COLOURS, 2) if not {a, b} <= FIXED]
    d, a, b = min(pairs)
    print(f"  {label:13s} {d:5.1f}  {a} / {b}")
