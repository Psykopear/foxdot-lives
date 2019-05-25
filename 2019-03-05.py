FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.hungarianMinor
Root.default=var(P[0], 1)
m = Master()
SynthDefs

s1.stop()
s2 >> sitar(s1.degree, dur=PDur(12,16), delay=0, sus=0.6, chop=4, oct=(4), amp=1)
b1 >> evilbass(s2.degree, amp=0.6, sus=0.4, oct=(4), dur=PDur(11,16)*2).stop()
s1 >> varsaw(P[0,0,0,0].shuffle().mirror(), chop=4, oct=(6), amp=0)
d1 >> play("h", echo=(0,0.1), mix=0.5, room=0.4, formant=sinvar([0,1],16), hpr=0.2, hpf=PWhite(100,2000), sample=PRand(list(range(5))), pan=PWhite(-0.8,0.8), amp=PWhite(0.8,1.0)*0.5, dur=PDur(11,16))
k1 >> play("X  XX X ", sample=(2), room=(0,0.4), mix=(0,0.5), shape=(0,0.2))
d2 >> play("h o ").sometimes("amen")


m.hpf=expvar([100,3000],16,start=now);m.hpr=0.2;m.mix=0.4;m.room=0.4;
m.hpf=0;m.hpr=1;m.mix=0;m.room=0;
