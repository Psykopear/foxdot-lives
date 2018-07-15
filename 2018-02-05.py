from FoxDot import *

Scale.default=Scale.phrygian
Root.default=var([0,3,2,1], [8,2,2,2])

s1 >> pluck(0, dur=0.25, chop=1, formant=(0,PWhite(0.2, 1)), hpf=linvar([100,1000], 16), hpr=0.2, shape=(0.2,0))
b1 >> evilbass(s1.degree, amp=P[0,1,1,1]*3, dur=PRand([0.25]), sus=0.3)

k1 >> play("X ", sample=2, amp=2, hpr)
d1 >> play("h", echo=0.2, dur=1, sample=PRand(list(range(10))), amp=PWhite(0.8,1))

Clock.bpm=200
