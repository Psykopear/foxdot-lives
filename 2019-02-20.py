FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

s1 >> play("x-o-").sometimes("amen")
k1 >> play("X ", sample=2).seomtimes("stutter", 4, dur=2)
b1 >> evilbass(P[0,0,0,0,1], amp=0.6, oct=4, dur=PDur(P[5],8))
