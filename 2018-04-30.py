from FoxDot import *

Scale.default=Scale.locrian

s1 >> klank(b1.degree, chop=4)
k1 >> play("(X [XX])(x-)(t-[-])", hpf=PWhite(500,2000), hpr=0.2, dur=0.25, amp=0.4, sample=2).stop()
k2 >> play("x--", dur=Fraction(1,3), sample=5, amp=1.2)
b1 >> evilbass(PRand([1,0,0,2,0,0]), dur=Fraction(1,3), amp=PEuclid(5,6)*1.5)
d1 >> play("- o ", sample=PRand(list(range(2))), echo=0.2, mix=0.3, room=0.3)
s1 >> sitar((b1.degree, b1.degree + 1), dur=Fraction(1,3), chop=2, amp=PEuclid(10,16)*0.8, oct=(5), shape=(0,0.3))


Group(s1,k1,b1).solo()

Clock.bpm=180

Master().hpf=500;Master.hpr=0.3;Master.mix=0.2;Master.room=0.3

b3 >> evilbass(sus=0.2, dur=0.5, amp=PEuclid(2,4), delay=0.5)
k3 >> play("X ", sample=2, shape=(0,0.8))
d1 >> play(" (- ) ( -)")
Group(k3,b3).solo()
