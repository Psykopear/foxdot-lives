FoxDot.start
from FoxDot import *

Clock.clear()
Scale.default = Scale.phrygian
Root.default = var(P[0], 1)
m = Master()
Clock.bpm = 160

SynthDefs
s1 >> orient(
    var([0, 1], 8),
    dur=PDur(3, 8) * 1,
    sus=1,
    chop=4,
    formant=(0, sinvar([3, 1], 16)),
    oct=4,
    hpr=0.2,
    hpf=sinvar([100, 1000], 16),
    amp=PWhite(0.5, 1) * expvar([0.5, 1], 0.5),
    pan=sinvar([-0.8, 0.8], 32),
).every(6, "stutter", 4, dur=3)
s2 >> sitar(
    s1.degree + PRand([0, 0, 0, 2, 4]),
    dur=PDur(11, 16) * 2,
    amp=0.8 * expvar([0.5, 1], 0.5),
    sus=0.2,
    shape=(0, 0.2),
    oct=(4, 5),
)
d1 >> play(
    "--*-", sample=2, dur=0.5, pan=PWhite(-0.8, 0.8), amp=PWhite(0.8, 1.2)
).sometimes("amen")
b1 >> sawbass(s2.degree, sus=0.3, cutoff=900, dur=PDur(5, 8), amp=expvar([0.5, 1], 0.5))
k1 >> play("X ", sample=5, shape=1, room=0, mix=0, echo=0, amp=2.0).sometimes(
    "stutter", 4, dur=3
).sometimes("amen")
