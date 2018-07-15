from FoxDot import *

Scale.default=Scale.egyptian

s1 >> klank(P[0,0,2,0, 1,0,-2,0, 0,3,1,2, 3,2,1,0], chop=4, sus=s1.dur, dur=1, shape=(0,0.2))
b1 >> evilbass(s1.degree, dur=0.25, oct=(4,5), amp=P[0,1,0,1, 1,0,1,1, 0,1,1,1, 0,0.5,0.8,1], sus=0.5)
k1 >> play("<{X } {x }><  l h  i >", amp=1, sample=2, hpf=PWhite(200,1000), dur=0.25, mix=0.3, room=0.2)
k2 >> play("x ", sample=5)
d1 >> play("- h - ", chop=4, hpf=200, hpr=0.2, amp=1.3)
k1.stop()


Master().hpf=500;Master().hpr=0.2;Master().mix=0.2;Master().room=0.1

Clock.bpm=170


Scale.default=Scale.phrygian

s2 >> pluck(P[0,0,PRand([1,2,0,3])], oct=(4,5,6), chop=3, shape=0.3, amp=1.4)
b2 >> evilbass(s2.degree, dur=Fraction(1,3), amp=P[0,1,1]*2, sus=0.3)
k3 >> play("X ", sample=2)
d1.reset() >> play("-", sample=PRand([0,1,2,3,4,5]), pan=PWhite(-0.8,0.8), dur=PRand([0.5,0.25]), amp=PRand([0,1,1,1]))
Group(k3,b2).stop()
Group(s2,b2,k3).stop()


Master().amplify=var([1,1],[.25,.25])

# sorry
k1.reset() >> play("<X >< ( -)o(- )>", sample=2, amp=1.4).every(8, 'stutter', PRand([1,2,3]))
b1.reset() >> bass(s1.degree, dur=0.5, amp=P[0,1]*1.2)
s1.reset() >> prophet(0, oct=(4,5), chop=4, shape=(PWhite(0.3,0.7),0))

# yeah closing
Master().room=0.4;Master().mix=0.4;Master().formant=0.9

