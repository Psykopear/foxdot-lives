FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

s2 >> pluck(s1.degree + PRand([0,0,0,0,0]), chop=1, dur=PDur(P[3,4,5,4],8), sus=0.7, oct=(4,5))
b1 >> dbass(s1.degree, dur=PDur(P[4,3,4,5],8), sus=0.3, amp=1)

d1 >> play("h-(ooooooOO)(-[--])", dur=0.25, hpf=PWhite(200,3000), echo=(0,0.1), amp=(1.0,0.2), hpr=0.3, mix=0.3, room=0.4).sometimes("amen")
s1 >> ambi(var([0,0,-1,1],8), hpr=0.3, hpf=sinvar([100,3000],16), chop=4, shape=(0,sinvar([0,0.4],8)), room=0.3, mix=0.3, amp=1.2)
Group(b1,s1,s2,k1).solo()
k1 >> play("V ", sample=0, mix=(0,0.7), room=0.4, amp=(1.3, 0.8))
g = Group(b1,s1,s2,k1)
g.hpf=0;g.hpr=0.2

m.hpf=expvar([100,3000],16);m.hpr=0.3;m.mix=0.2;m.room=0.2
m.hpf=0;m.hpr=1;m.mix=0.0;m.room=0.0



