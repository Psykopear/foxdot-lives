from FoxDot import *

Clock.clear()

Scale.default=Scale.phrygian

s1 >> prophet(var([0,3,-1],[8,4,4]), shape=0.3, dur=4, sus=4,oct=(3,4,5), chop=16 )
d1 >> play("X-<X><o>-", sample=2, room=(0,0.4), mix=(0,0.4)).sometimes("amen").spread()
b1 >> evilbass(s1.degree, sus=0.4, dur=PDur(P[3,4,5,3],8), amp=0.8, oct=4)

Master().hpf=0
