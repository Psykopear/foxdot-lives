FoxDot.start
from FoxDot import *
import FoxDot
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

a1 >> audioin()
m1 >> MidiOut(1, channel=1)
midi
