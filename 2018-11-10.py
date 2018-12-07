FoxDot.start
from FoxDot import *

Clock.clear()
Scale.default = Scale.phrygian
Root.default = var(P[0], 1)
m = Master()

s1 >> prophet(var([0, 2, 1, -1, 0], 8), dur=PDur(3, 8) * 2, oct=(4, 5)).spread()
