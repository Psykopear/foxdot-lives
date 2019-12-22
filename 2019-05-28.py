from FoxDot import *

Scale.default=Scale.justMinor

Clock.bpm=134

Clock.clear()
Root

print(Scale.phrygian)


d1 >> play("h-h8", mix=(0,1), room=0.3, dist=(0,1), formant=(0,PWhite(0,7)), sample=2).sometimes("stutter", 3, dur=1, hpf=500, hpr=0.2)
d2 >> play("X[xx]", sample=2, shape=(0,0.3))
s1 >> ambi(var([0,2,1],[8,4,4]), shape=(0,PRand([.1,.2,.3,.4,.5])), chop=4)
b1 >> evilbass(s1.degree, sus=0.2, dur=PDur(3,8), oct=4, amp=0.5)


d1.reset() >> play("V+")
d1.amplify = sinvar([1,0],2)
d2.reset() >> play("mi  u   ", echo=(0,0.1), room=0.4, mix=(0,0.7), hpf=PWhite(100,3000), hpr=0.4, formant=PWhite(0,4), dur=0.25)
b1.reset() >> evilbass(var([0,0,1,-1],[8]), sus=0.4, dur=PDur(5,8), oct=(4), amp=P[0.3,0.5,0.6,0.3])


