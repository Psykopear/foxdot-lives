FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

s1 >> razz(var([0,0,-1,1], 4), oct=(4,5), shape=0.2, dist=0.2, room=0.1, mix=0.1, dur=PDur(P[5,9,7,8],16), hpr=0.2, sus=0.1, hpf=sinvar([20,1000],16))
b1 >> evilbass(s1.degree, oct=4, dur=PDur(P[11,13,9,8],16), amp=P[1]*0.3, cutoff=expvar([100,5000],32), sus=0.5)
k1 >> play("X-hX(-X)(X[--])", sample=2, amp=1, mix=(0,0.3), room=0.4, shape=(0,0.3))


Group(s1,b1,k1).hpr=0.1;Group(s1,b1,k1).hpf=expvar([6000,10000],1,start=now);


s2 >> sitar(var([0,3,2,0,-1,2], [4,2,2]), dur=PRand([0.5,1]), chop=4, sus=2).stop()
s3 >> sitar(var([0,3,2,0,-1,2], [4,2,2]), dur=0.25, chop=0, sus=0.2, amp=0.9, hpf=500, hpr=0.1, oct=4)

d1 >> play(" r t", echo=(0,0.1), room=0.4, mix=0.3, amp=(2,0.3)).sometimes("amen").sometimes("stutter", 3, dur=2)
k2 >> play("V(waawaaw)", mix=(0,0.9), room=0.4, shape=(0,0.2), dist=(0.1,0), amp=(1,0.3))
b1.reset() >> evilbass(0, oct=(4), sus=0.3, dur=PDur(5,8), amp=1)
