from FoxDot import *

Scale.default=Scale.phrygian

s1 >> klank(P[0,PRand([0,1,2,3,4])], chop=4)
b1 >> evilbass(s1.degree, dur=0.5, delay=0.5, amp=PEuclid(4,8), sus=0.2)
b1 >> dab(sus=1, dur=PRand([1,0.5]))
k1 >> play("<  - ><(-[--])  h   >", dur=1/3, sample=2, room=0.2, hpf=PWhite(100,2000), hpr=0.2).every(4, 'stutter', 5)
d1 >> play("  - ", sample=5, dur=0.25)


Master().hpf=19900;Master().hpr=0.3


Clock.bpm=143

k2 >> play("Vr-", dur=Fraction(1,3), echo=0.0)
b3 >> sawbass(P[0,PRand([0,1,2,3,4])], dur=Fraction(1,3), amp=PEuclid(7,9)*1.2, sus=0.1)
Group(k2,b3).solo()



