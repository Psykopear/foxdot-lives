FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

SynthDefs

s1 >> prophet(var(P[0,(0,P[0,3,1,8])],4), formant=sinvar([0.1,4],6), shape=sinvar([0.1,0.2],8), oct=(4,5), dur=4, chop=(0,16))
s2 >> zap(s1.degree, dur=PDur(3,8)*2, sus=5, pan=sinvar([-1,1],3)).spread()
d1 >> play("-", sample=PRand(list(range(5))), dur=0.25, amp=PEuclid(11,16)*PWhite(0.9,1.1), pan=PWhite(-1,1))
b1 >> sawbass(s1.degree[-1], dur=PDur(3,8)*1, sus=0.3, room=(0,0.5), mix=(0,1))
k1 >> play("Xb", sample=2, amp=1.1, room=(0,0.6), mix=(0,1), shape=(0,0.1)).sometimes('stutter', 4, dur=3)
d2 >> play("  |*3| ").spread()
