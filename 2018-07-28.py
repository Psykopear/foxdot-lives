FoxDot.start

from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

s1 >> klank((0,var([3,2,1,7],16)), dur=0.25, formant=sinvar([0,1],16), shape=sinvar([0.5,0],16), chop=PRand([1,2]), amp=0.8)

s2 >> pluck(s1.degree[1] + P[-1,-2,-3,1,0,0,0,0,0,0].shuffle(), dur=0.25, amp=PEuclid(P[7,8,9,10],16))

b1 >> bass(s2.degree, sus=0.25, dur=0.25, amp=PEuclid(P[7,8,9,10],16)*1.0, shape=(0,0.1), hpf=0, lpf=0)#expvar(100,1000,1/4), lpr=0.3)
d2 >> play(" (h )o ", room=0.4, mix=(0,0.4))
k1 >> play("X ", sample=2, shape=(0,0.1), formant=(0,0.1), hpf=(0,0), hpr=0.3, echo=(0,0.1)).every(8, 'stutter', PRand([1,2,2])),

Group(k1,b1,s1,s2,d1,d2).stop()
mix = Group(s1,s2,d1,d2,k1,b1)
mix.hpf=300;mix.hpr=0.1;mix.mix=0.6;mix.room=0.4;

Clock.bpm=134
Root.default=var([0,3],8)
(
    k2 >> play("X--", amp=1, dur=1/3, room=(0,0.4), mix=(0,0.4), sample=2),
    d4 >> play("hhOh", amp=1),
    d1 >> play("<-><h>", delay=PRand([0.01,0.02,-0.01,-0.02,0]), sample=list(range(5)), pan=PWhite(-1,1), dur=1/3, amp=PEuclid(9,12)*PWhite(0.8,1)).stop(),
    b2 >> sawbass(s4.degree + P[1,0,0,0,3,0,0,0,2,0,0,0,4,0,0,0], dur=1/3, sus=0.1, amp=2),
    s3 >> sitar(b2.degree, amp=PEuclid(P[5,8,9],12)*1, hpf=PWhite(0,1000), hpr=0.3, sus=0.2, echo=0.0, dur=1/3, chop=0),
    s4 >> fuzz(0, shape=(0.8,0), amp=2, chop=P[0,1,2,3,4], hpf=4000).stop(),
)
mix = Group(k2,d1,s4,s3)
mix.solo()
drums = Group(k2,d4,d1)
drums.amplify=var([1,0],28,4)

m.hpf=300;m.hpr=0.1;m.mix=0.2;m.room=0.4;
m.hpf=0;m.hpr=0;m.mix=0;m.room=0;
