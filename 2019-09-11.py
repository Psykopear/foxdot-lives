from FoxDot import *


Clock.clear()

Scale.default=Scale.phrygian

d1 >> play("= -[--]  h-", echo=0, sample=1, room=0.5, mix=0.5).spread().stop()

k1 >> play("this-is-docler", rate=PRand([2,1,-0.5,1]), sample=0, dur=0.25, amp=0.0, mix=0.5, room=0.5, hpr=0.1, hpf=(0,PWhite(300,1000)), dist=(0,1))

s1 >> klank(b1.degree + (0,0,P[0,1,2,3,-1,0,2,1]), oct=(3,4,5), chop=(0,4,8), shape=sinvar([0,0.9], 32), formant=sinvar([1,0], 32), hpr=0.1, hpf=sinvar([100,1000], 32), amp=0.0, pan=sinvar([-1,1],16))

Clock.bpm=80*2

d2 >> play("{-s}{[ss][--][s-][-s]}", amp=1, rate=P[1,-1], pan=(0,PWhite(-1,1))).spread().often("amen")
d3 >> play("  O[--]", dur=0.5, room=0.5, rate=P[1,-1,1],mix=(0,0.9))
b1 >> evilbass(var([0,0,0,1],4) + (0,7), dur=PDur(P[3,5,4,7],8), sus=0.4, oct=4, amp=expvar([0,1],0.5))
k2.reset() >> play("Xh", rate=(1), sample=2, amp=2, shape=(0,0.4,0.1), formant=0, hpf=(0,300), hpr=0.2).often("stutter", 4, dur=1, hpf=PWhite(500,1000))
