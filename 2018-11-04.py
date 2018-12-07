FoxDot.start
from FoxDot import *

Clock.clear()
Scale.default = Scale.phrygian
Root.default = var(P[0], 1)
m = Master()

s1 >> prophet(
    (0, P[0, 2, 1, -1]),
    dur=PDur(3, 8) * 8,
    oct=(4, 5),
    formant=sinvar([0, 1], 16),
    chop=16,
    shape=(0, sinvar([0, 0.8], 16)),
).sometimes("stutter", 4, dur=3).spread()
b1 >> sawbass(s1.degree[1], dur=PDur(3, 8), sus=0.3, amp=2, hpr=0.2, hpf=0)
k1 >> play("X|-1|-X|-1|-X-", sample=2, amp=0)
k2 >> play("|V0||-3|", sample=5, amp=2).sometimes("stutter", 4, dur=3)
