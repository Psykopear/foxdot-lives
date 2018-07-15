from FoxDot import *

Scale.default=Scale.justMinor

s1 >> arpy(P[0,PWhite(-7,7,True)], dur=0.25, formant=(0,PWhite(0.2,0.8)), sus=0.6)
s2 = Player()
s2 >> pluck(s1.degree, dur=0.25, echo=0.1, amp=PRand([1,0]))
d1 >> play("X  x o")
