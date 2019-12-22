from FoxDot import *

Clock.clear()

Scale.default=Scale.major


s3 >> varsaw(var([0,-2,-1], [10,5,5]), shape=P[.8,0,.2,0,.3,0,0.4,0], amp=1.0, sus=((0.08),(0.3)), mix=(0,1), room=0.5, oct=((3,4), (3,4)), dur=PDur(5,10))
d1 >> play("{kh}", sample=2, rate=PRand([1,-1]), dur=PDur(6,10))
b1 >> evilbass(s3.degree, sus=0.4, dur=PDur(5,10), delay=0, amp=0.5, oct=4)
k1 >> play("XhhXr", dur=0.5, hpf=0, hpr=0.2, sample=2)
d2 >> play("=i*td", room=0.5, mix=(0,0.9))

s3 >> varsaw(var([0,-2,-1], [8,4,4]), shape=P[.8,0,.2,0,.3,0,0.4,0], amp=1.0, sus=((0.08),(0.3)), mix=(0,1), room=0.5, oct=((3,4), (3,4)), dur=PDur(5,8))
d1 >> play("{kh}", sample=2, rate=PRand([1,-1]), dur=PDur(6,8))
b1 >> evilbass(s3.degree, sus=0.4, dur=PDur(5,8), delay=0, amp=0.5, oct=4)
k1 >> play("XhXr", dur=0.5, hpf=0, hpr=0.2, sample=2)
d2 >> play("=itd", room=0.5, mix=(0,0.9))

Master().hpf=0;

Master().hpf=900;Master().hpr=0.1

Root.default=var([0,2],16)
Scale.default=Scale.major

s2 >> pluck([(0,2,4)], dur=PDur(3,8))
