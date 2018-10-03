FoxDot.start
from FoxDot import *

Clock.clear()
Scale.default = Scale.phrygian
Root.default = var(P[0], 1)
m = Master()


s2 >> pluck(
    s1.degree + PRand([0, 1, 2, 3, 0, 0, 0, 4]),
    oct=4,
    dur=0.5,
    sus=0.5,
    amp=PEuclid(11, 16) * 1.0,
    room=(0, 0.4),
    shape=0.1,
)
s3 >> pluck(
    s1.degree + PRand([0, 1, 2, 3, 0, 0, 0, 4]),
    oct=5,
    dur=0.25,
    sus=0.5,
    amp=PEuclid(11, 16) * 1.0,
    room=(0, 0.4),
    shape=0.1,
)

(
    s1
    >> klank(
        var([0, 1, 3, 2], 12),
        lpf=1600,
        room=(0, 0.5),
        mix=(0, 0.6),
        shape=(sinvar([1, 0.3], 6), 0.1),
        amp=.9,
        chop=PRand([1, 3, 9]),
        formant=sinvar([1, 0], 12),
    ),
    d2 >> play("X--", dur=1 / 3, sample=2, lpf=0, dist=(0, 0.5)),
    s4
    >> fuzz(
        s2.degree,
        amp=0.5,
        shape=0.5,
        hpf=sinvar([100, 4000], 12),
        hpr=0.1,
        dur=1 / 3,
        chop=PRand([1, 3, 9]),
    ),
    d3 >> play("  o "),
    d1
    >> play(
        "-",
        sample=PRand(list(range(5))),
        amp=PWhite(0.8, 1.2) * PEuclid([8, 9, 11, 5], 12),
        pan=PWhite(-1, 1),
        dur=1 / 3,
    ),
    b1
    >> evilbass(
        s1.degree,
        dur=1 / 3,
        sus=0.4,
        oct=(4, 5),
        amp=PEuclid(P[9, 11, 8, 10], 12) * 1.2,
    ),
)
