from FoxDot import *

Root.default = var([3,4,3,6,4,1],[8,8,8,4,2,2])
Clock.default=140


s1 >> prophet(chop=3, oct=(4,5), hpf=PWhite(100,2000), hpr=0.2).every(8, 'stutter', 2)
b1 >> sawbass(oct=5, dur=Fraction(1,3), amp=P[0,1,1, 0,1,0, 1,0,1, 0,1,1]*3, sus=0.15, rq=0.2, cutoff=900)
d1 >> play("-", dur=Fraction(1,3), sample=PRand([0,1,2,3]), amp=PRand([0,1]))
d2 >> play("X-", sample=2, amp=1.5)
d3 >> play("  o ", amp=1.4)

group = Group(s1,b1,d1,d3)

group.hpf=0;
