from FoxDot import *

Clock.bpm = 140

Scale.default=Scale.locrian

Root.default=var([0,2,0,2,1],[8,8,8,4,4])

b1 >> bass(b2.degree, dur=0.25, sus=0.4, hpr=0.1, hpf=(PWhite(0,1000),PWhite(1000,2000)), pan=(PWhite(0,1),PWhite(1,0)), shape=0.8, formant=0.2)
b2.reset() >> sawbass(PRand([0,0,0,0,2,3]), dur=0.25, sus=0.1, amp=P[0,1,PRand([0,1]),1]*2)

c1 >> viola(chop=PRand([1,2,4]), oct=P[5,6], amp=2)

print(SynthDefs)

Group(b1,b2,c1).solo()
Group(b1,c1).room=0.3;Group(b1,b2,c1).mix=0.3;Group(b1,b2,c1).shape=0.9;

d1 >> play("(- [--]-)", dur=0.5, sample=2, hpf=(PWhite(100,1000),PWhite(1000,2000)), hpr=0.2, amp=2)
b1.amplify=expvar([0.0,0.7],0.5)
Group(b1,c1).amplify=expvar([0.0,1],0.5)
d2 >> play("  O ", dur=0.5)
d3 >> play("-", dur=0.25, sample=PRand([1,2,3,4,0]), hpf=PWhite(0,2000), hpr=0.2, amp=PRand([0,4]))
k1 >> play("X ", sample=5, amp=3)
Master().hpf=0;Master().hpr=0.3


