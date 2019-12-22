from FoxDot import *

Clock.clear()

Scale.default=Scale.locrian

Root.default=-5

s1 >> razz(P[[0]*8+[2,2,2,2,1,1,1,1]], dur=1, chop=4, formant=(0,PWhite(0.4,0.9)))

b1 >> bass(s1.degree, oct=5, dur=0.5, sus=0.4, amp=P[0,1]*0.8)

k1 >> play("<X ><  o >", sample=2, shape=(0,0.2), mix=0.2, room=0.2)


d1 >> play("-", delay=PRand([0.01, -0.01, 0.02, -0.02, 0.005,0,0,0]), dur=0.25, amp=PRand([0,1,1]), sample=PRand(list(range(6))), pan=(PWhite(0,1), PWhite(-1,0)))


Master().bpm=120

Group(d1,s1).solo()

Group(b1,k1,s1).hpf=0

Group(b1,k1,s1).stop()#hpf=5000

Group(b1,k1).hpr=0.200


Scale.default=Scale.phrygian

s2 >> ambi(b2.degree, amp=1, echo=0.1, chop=8, shape=(0,0.3))
d1 >> play("-", hpf=linvar([100,1000],16), hpr=0.2, delay=PRand([0.01, -0.01, 0.02, -0.02, 0.005,0,0,0]), dur=Fraction(1,3), amp=PRand([0,1,1]), sample=PRand([4,3]), pan=(PWhite(0,1), PWhite(-1,0)))
b2 >> evilbass(0, dur=Fraction(1,3), amp=P[PRand([0,1]),1.8,2], sus=0.5)
d2 >> play("X ", amp=(1,0.4), room=0.2, mix=0.1, echo=(0,0.2), hpf=(0,400), sample=2).every(8, 'stutter', 4)
d3 >> play("  O ", amp=0.5)


Group(d3,b2).formant=0.9

Master().lpf=0
Master().lpr=0.2
