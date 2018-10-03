FoxDot.start
from FoxDot import *

Clock.clear()
Scale.default = Scale.phrygian
Root.default = var(P[0, 0, 0], 8)
m = Master()


s1 >> klank((0, P[7, 3, 1, 2]), dur=1, chop=4)
s2 >> sitar(
    PRand([0, 0, 0, 0, 0, 1, 3]),
    dur=0.25,
    sus=0.2,
    amp=PEuclid(11, 16) * 0.9,
    hpf=PWhite(200, 3000),
    chop=0,
)
(
    d1 >> play("-", dur=0.25, amp=PEuclid(11, 16), sample=PRand(list(range(5)))),
    d2 >> play(" (ho)(oh) ", mix=0.4, room=(0, 0.4)),
    k1 >> play("X ", sample=2, hpf=0, mix=(0, 1), room=(0, 0.3), amp=1.9),
)
b1 >> evilbass(s2.degree, sus=0.5, amp=PEuclid(P[9, 11, 13], 16) * 1.2, dur=0.25)


m.hpf = sinvar([200, 3000], 16)
m.hpr = 0.3
m.room = 0
m.mix = 0
m.hpf = 0
m.hpr = 0.3
m.room = 0
m.mix = 0
