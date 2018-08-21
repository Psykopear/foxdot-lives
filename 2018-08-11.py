FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()
Clock.bpm=120
Root.default=5

(
    d1 >> play("= (ho)(o -)", echo=(0,0.1), hpf=(0,sinvar([100,3000],20)), room=(0,0.4), mix=(0,0.5), amp=(1,0.7)),
    k1 >> play("= ", sample=2, shape=(0,0.1), amp=0.7),
    d2 >> play("-", dur=0.25, pan=PWhite(-1,1), sample=PRand(list(range(5))), delay=PRand([0.01,0.02,-0.02,-0.01,0,]), amp=PEuclid(P[11,14,9,12],16)*PWhite(1,0.8)),
    s1 >> sitar(var([0], 4)+PRand([0,0,0,0,0]), chop=0, shape=(0,0.1), oct=(4,5), sus=0.2, dur=0.25, amp=PEuclid(P[11,14,9,12],16)*0.7),
)


Group(k1,s1).solo()
