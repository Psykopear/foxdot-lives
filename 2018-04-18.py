from FoxDot import *

Clock.clear()

Scale.default=Scale.locrian

s1 >> ambi((b1.degree, b1.degree + 2), chop=2, formant=(0,0.9))
d1 >> play("h", dur=Fraction(1,3), sample=PRand(list(range(5))), amp=PEuclid(5,6))
b1 >> evilbass(0, sus=0.2, dur=PRand([1/3]), amp=PEuclid(7,12)*0.2)
k1  >> play(" -[  ]", dur=Fraction(1,3), sample=2)
