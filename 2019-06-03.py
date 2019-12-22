from FoxDot import *

Clock.clear()

Scale.default=Scale.phrygian

s1.reset() >> klank(var([0,0,1,-1],16), chop=(0,4), dist=0.0, shape=0.8, oct=(3,4), amp=.9).spread()
d1.reset() >> play("=--k+ - ", room=(1), mix=(0,1), echo=1, rate=PRand([1,-1,.2,1,.3,-.2])).spread()
s2.reset() >> pluck((s1.degree, s1.degree + 2), dur=PDur(P[2,4,8].stutter(4).shuffle().palindrome(),16), sus=16)
k1.reset() >> play("X(**)X([ *] )", hpr=0.1, hpf=0, sample=2)

m.hpr=0.5;m.hpr=0;m.room=0;m.mix=0

m=Master()

m.hpr=0.2;m.hpf=300;m.room=0.5;m.mix=0.5

