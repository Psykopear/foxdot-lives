from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()
d1 >> play("x-o-").every(7.5, "jump", cycle=8, sample=2, delay=var([-0.25, 0],8))
