from FoxDot import *

Scale.default=Scale.phrygian

Clock.clear()

Clock.bpm=130

s1.reset() >> razz(oct=5, dur=P[1])


d1 >> play("h-f-", rate=P[1,0.2,2,-1,.3,-.2]).sometimes("amen")
k1 >> play("X[-o]", sample=2, shape=(0,0.1))
b1 >> evilbass(s1.degree, oct=(4,5),shape=0.0, dur=PDur(3,8), sus=0.4)
s1 >> sitar(var([0,2,-1,1],8), oct=(4,5), dur=PDur(P[3,4,5,4],8))
