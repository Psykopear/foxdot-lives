from FoxDot import *

Clock.clear()

Scale.default=Scale.minorPentatonic


a1.reset() >> audioin(formant=(0, 0.2), lpf=(10000,500), lpr=0.2, mix=(0,0.8), dist=0, dur=1, room=0.9, shape=(0,0.05), amp=2, echo=0)

a1.reset() >> audioin(formant=(0, 0.2,0.6), lpf=(100,4000), lpr=0.83, mix=(0,0.8), dist=0.5, dur=1, room=0.9, shape=(0,0.05), amp=6, crush=1)

a1.reset() >> audioin(amp=0.6, lpf=(20000,50), lpr=0.1, room=0.9, mix=(0,0,1)).spread()

d1 >> play("<X-->", dur=1/3, mix=(0,0,0.9,0.9),sample=2, amp=(2,1), room=0.4, hpf=0).sometimes("amen").solo()

b1 >> evilbass(var([0,5,3,1],[8,4,2,2]),hpf=0,  oct=(3,4),dur=PDur(P[3,4,5,4],6), sus=0.4, amp=0.8).solo()

s1 >> sitar(b1.degree, dur=PDur(4,6), amp=1, sus=0.3, oct=(4,5), hpf=PWhite(100,1000), hpr=0.1).spread().solo()

b1 >> sawbass(var([0,0,0,1], 8), dur=PDur(3,8), sus=0.3, )

p1 >> pluck((b1.degree, b1.degree + 2), dur=PDur(P[3,4,5],8))
s1 >> prophet()

s2 >> sitar(mix=0.5, room=0.3, strum=0.3, echo=(0,0.25))
