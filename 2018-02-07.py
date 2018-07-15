from FoxDot import *

Scale.default=Scale.phrygian
Root.default=var([0,5,3,1],[10,2,2,2])
Root.default=5#var([0,5,3,1],[10,2,2,2])

s1 >> pluck(oct=(4,5), dur=0.5, amp=PEuclid(5,8), chop=2, pan=PWhite(-0.8,0.8))
s2 >> arpy(amp=PEuclid(13,16)*2, dur=0.5, formant=(0,0.2))

b1 >> evilbass(dur=0.25, amp=PEuclid(11,16)*1, delay=0, sus=0.3, rq=0.2, cutoff=900)
k1 >> play("x ", sample=5, amp=0.8)
d1 >> play("-", sample=PRand(list(range(6))), dur=P[0.25,0.5,0.25], amp=PRand([0,1.2]), delay=PRand([0.001,-0.001,0]))
d2 >> play("  O ", room=0.4, mix=0.4, amp=0.6)

Master().hpf=700
Group(b1,k1).hpr=0.2


s3 >> sitar(P[0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,1,1], chop=4, oct=(4,5), formant=(0,PWhite(0,1)))
d1.reset() >> play("X o(xh)", hpf=400, echo=(0,0.2), amp=(2,0.4))
k1 >> play("<X-><    >", sample=2, amp=2)
b1 >> sawbass(s3.degree, amp=P[0,0,1,1]*2, dur=0.25, sus=0.2, oct=(4))
s4 >> varsaw(s3.degree, oct=(4,5), dur=0.25, chop=2, shape=(0,PWhite(0,1)), pan=PWhite(1,-1))

Master().room=0.3;Master().mix=0.3;Master().hpr=0.9;Master().hpf=300;

Clock.bpm=140


Scale.default=Scale.minorPentatonic

k5 >> play("( o)(-h-)(o--)", hpf=PWhite(300,2000), amp=PRand([0.2,0.8,1]), hpr=0.3, sample=1, dur=Fraction(1,3))
k6 >> play("X ", sample=2, amp=1.4, shape=(0,0.2))
b5 >> bass(var([0,2,3,1],[10,2,2,2]), sus=0.2, dur=Fraction(1,3), amp=P[0,1,1,1]*0.8)
s5 >> prophet(b5.degree, chop=3, amp=1.3, oct=(4,5), mix=0.3, shape=(0,0.2), sus=0.6)


Group(k5,b5,s5).solo()
