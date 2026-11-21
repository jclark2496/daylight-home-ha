"""WCAG 2.x contrast check for the Daylight Home palette. Run: python3 tools/contrast.py"""
def lum(h):
    h = h.lstrip('#'); r, g, b = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)
def ratio(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + 0.05) / (lb + 0.05)
# (name, foreground, background, minimum) - 3.0 is the WCAG minimum for large/bold text and icons
pairs = [
  ("primary text on card", "#172033", "#FFFFFF", 4.5),
  ("primary text on page", "#172033", "#F6F8FB", 4.5),
  ("muted label on card", "#5F6B7A", "#FFFFFF", 4.5),
  ("muted label on page", "#5F6B7A", "#F6F8FB", 4.5),
  ("blue accent icon on card", "#2F67E8", "#FFFFFF", 3.0),
  ("rose accent icon on card", "#B21B65", "#FFFFFF", 3.0),
  ("white hero name on blue (light end)", "#FFFFFF", "#247CF4", 3.0),
  ("white hero name on rose (light end)", "#FFFFFF", "#D81B7A", 3.0),
  ("white hero name on blue (dark end)", "#FFFFFF", "#4056D8", 4.5),
  ("white hero name on rose (dark end)", "#FFFFFF", "#94184F", 4.5),
]
bad = 0
for n, a, b, m in pairs:
    r = ratio(a, b); ok = r >= m; bad += not ok
    print(f"{r:5.2f}:1  {'PASS' if ok else 'FAIL'} (min {m})  {n} ({a} on {b})")
raise SystemExit(1 if bad else 0)
