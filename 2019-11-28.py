from FoxDot import *

Scale.default = Scale.phrygian

s3.reset() >> pluck(
    PChain({-1: [0], 0: [0, -1, 2], 1: [3, 2], 2: [0, 1], 3: [0]}),
    oct=(3, 4, 5),
    hpf=PWhite(200, 2000),
    hpr=0.2,
    shape=0,
    mix=0.5,
    room=PIndex() % 2,
    formant=PIndex(),
    dur=PDur(P[5, 4, 3], P[8, 7, 6]),
    pan=PWhite(-1, 1),
).spread()

b1 >> evilbass(
    s3.degree,
    dur=PDur(P[5, 4, 3].reverse(), P[8, 7, 6].reverse()),
    oct=4,
    sus=0.6,
    amp=2.0,
    cutoff=PWhite(200, 2000),
)
k1 >> play("<X ><V >", sample=(2, 0), amp=2, shape=(0, 0.1), mix=(0, 1), room=(0, 0.4))

Clock.clear()
