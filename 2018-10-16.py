FoxDot.start
from FoxDot import *

Clock.clear()
Scale.default = Scale.phrygian
Root.default = var(P[0], 1)
m = Master()

s1 >> klank()
d1 >> play("X ")
