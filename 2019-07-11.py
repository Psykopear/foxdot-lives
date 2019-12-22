from FoxDot import *

Clock.clear()

Scale.default=Scale.major

Clock.bpm=120

SynthDefs

s1 >> orient(P[0,2,4,6,7,6,4,2], oct=(4,5), amp=0.4, chop=4)
b1 >> evilbass(var([(9,13),(0,7),(2,9),(0,7),(1,8),(2,9)],32), dur=PDur(3,8), sus=0.6, amp=0.3, oct=4, room=0.3, mix=0.4, chop=0)
d1 >> play("[****][****]", echo=(0,0.1), hpr=0.2, hpf=sinvar([100,3000],16), room=0.5, amp=0.3, mix=(0,0.9)).sometimes("amen")
k1 >> play("<X[xx]><h-o->", sample=2, amp=0.5).sometimes("stutter", 3, dur=1)
