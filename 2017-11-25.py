from FoxDot import *

Clock.bpm=130

Root.default=7

a1 >> audioin(room=0, mix=0.0)

s1 >> arpy(oct=(4,5))
s1.scale=Scale.chromatic
s1.root=var([0,7],[16,16])
s1.degree=P[2,2,2,3,3,3,0,0,3,2, 2,2,2,3,3,3,7,6,3,2]
s1.sus=2
s1.dur=P[.75,.75,.5, .75,.75,.5, .75,.75,.5, 2]
s1.amp=2


b1 >> sawbass(P[0],sus=0.05,oct=3,scale=Scale.chromatic)



s2 >> klank(s1.degree, scale=Scale.chromatic, room=0.6, mix=0.6)

d1 >> play("")
d1.degree="{-[--][-]}"
d1.dur=0.5
d1.amp=PWhite(0.2,1.2)
d1.dur=Fraction(1,3)


d2 >> play("  ")
b1 >> bass(PRand([s1.degree, s1.degree + 3]), scale=Scale.chromatic, dur=Fraction(1,3), amp=P[0.2,0.9,1.0]*1.0, sus=0.2, formant=(0, 0.2, 1))
