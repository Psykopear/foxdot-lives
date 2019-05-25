FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()
Clock.bpm = 80

a1 >> audioin(shape=0.0, room=(0,0.4), mix=(0,0.5))
d1 >> play(" ", mix=0.4, room=0.3, echo=(0,0.1), amp=(0.6,0.1), dur=PDur(P[5,4,3,4],8), sample=PRand(list(range(5))))
d2 >> play("x-").sometimes("amen")
b1 >> evilbass(P[-1,-1,-6,-6,7,7,2,4], scale=Scale.chromatic, dur=1,  amp=0.5, oct=(4)) 


