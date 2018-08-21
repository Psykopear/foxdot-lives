FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

s1 >> feel(PRand([0,1,2,3,4,0,0]), dur=(1,2,4), amp=1/3)
s2 >> sitar(s1.degree, dur=0.25, sus=0.2, amp=PEuclid(P[11,14,9,7].shuffle().mirror(),16)*0.7)
b1 >> evilbass(s1.degree[0], dur=0.25, amp=PEuclid(12,16), delay=0.5, sus=0.7)
d1 >> play("-", sample=PRand(list(range(6))), pan=PWhite(-1,1), dur=0.25, amp=PEuclid(P[10,11,12,14,13,15,16].shuffle(),16))
d2.reset() >> play("  o ", echo=(0), amp=0.7)
k1 >> play("X-", amp=1, shape=(0,0.1), sample=2).every(8, 'stutter', PRand([4,2,1]))
