FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()


s1 >> evilbass(oct=5, dur=4, sus=4, amp=2)
