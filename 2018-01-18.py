from FoxDot import *

Root.default=5
Scale.default=Scale.minorPentatonic


s1 >> evilbass(-0, oct=4, sus=0.3, dur=0.25, amp=P[0.3,0.4,0.8,1]*3.5)
k1 >> play("X ", sample=2, shape=(0,0.1), amp=1.5)
d1 >> play("  o ", echo=(0,0.2), room=(0,0.4), mix=(0.2,0.4), hpf=200, hpr=0.2)
d2 >> play("-", dur=(0.25), sample=PRand(list(range(5))), amp=PWhite(0.0,2.2), pan=PWhite(-0.7,0.7))
s2 >> ambi(s1.degree, chop=1, dur=0.25, formant=(0,PWhite(0.0,0.9)), shape=(PWhite(0.0,0.7),0), amp=0.3)
s3 >> sitar(s1.degree + PRand([0,0,0,1,2,3]), amp=PRand(P[0,1,1,1]*0.8), dur=PRand([0.25,0.5]), shape=PRand([0,0.8]), oct=(4,5), hpr=0.2, hpf=PWhite(200,2000), formant=0.2, chop=1)

Master().lpf=0
Master().lpr=0.4

Group(s1,k1,s3).solo()

Clock.bpm=140
