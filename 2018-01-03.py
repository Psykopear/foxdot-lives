from FoxDot import *

s1 >> klank(b1.degree, scale=Scale.locrian, dur=0.5, shape=PWhite(0,1), chop=PRand([2,4,8]), hpf=linvar([100,3000], 1), hpr=0.2, amp=expvar([0,1],1))
# s2 >> arpy(P[0,(0,12,16),(0,12,16),0,(12,15), 0,(0,12,15),(0,12,15),0,(12,16)], amp=P[1,1,1,1,1, 0,1,1,1,1], sus=0.5, dur=P[.5,.5,.5,.25,.25])
s2 >> arpy(b1.degree, scale=Scale.locrian, oct=6,  amp=P[1,1,1,1,1, 0,1,1,1,1]*2, sus=0.5, dur=P[.5,.5,.5,.25,.25])

d1.reset() >> play("-", dur=Fraction(1,3), sample=PRand([0,1,2,3,4]), pan=PWhite(-1,1), hpr=0.2, hpf=PWhite(100,1000))
d2 >> play("  h ", echo=0.1)
d3 >> play("- o (o )-")
d4.reset() >> play("(x ) (o ){xX}  ", sample=2, mix=0.2, room=0.2, hpf=200, hpr=0.2)

b1.reset() >> evilbass(PRand([0,3,0,2]), amp=1.2, scale=Scale.locrian, dur=PRand([0.25, 0.5]))
k1.reset() >> play("X ", hpf=0, sample=2, amp=1.2, shape=(0.8,0))


Master().hpf=700;Master().room=0.9;Master().mix=0.4;Master().hpr=0.2
Clock.bpm=134


Scale.default=Scale.phrygian
d1.reset() >> play("-", dur=Fraction(1,3), sample=PRand([0,1,2,3,4]), pan=PWhite(-1,1), hpr=0.2, hpf=PWhite(100,1000))
k2.reset() >> play("(o )  (  o )", shape=0.2, sample=5)
k3.reset() >> play("X ", sample=2)
Group(d1,k2,b2).amplify=var([1,0],[28,4])
b2.reset() >> sawbass(P[0,0,0,0,2,0,1,0], sus=b2.dur, dur=PRand([Fraction(1,3)]), amp=P[0,1,1, 0,0,1, 1,0,1, 1,0,1]*4)
s3.reset() >> sitar(b2.degree, chop=2, shape=0.2, mix=0.2, room=0.2, pan=PWhite(0.8,-0.8), dur=Fraction(1,3))

Group(k2,k3,b2,s3).solo()
