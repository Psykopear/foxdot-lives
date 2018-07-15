from FoxDot import *

from FoxDot import *

Scale.names()

print(dir(Scale))

Clock.clear()

a1 >> play('x_o__xox', sample=0, formant=PRand(list(range(10))), room=1, mix=0.2, spin=0, amp=0.5)

k1 >> play(PEuclid2(P[4,4,4,4, 4,4,3,7, 4,4,4,3, 4,4,6,8],8," ", "X"), sample=3, amp=4, room=0.2, mix=0.2)

d1 >> play('o   ', amp=0.7, room=1, mix=0.2)

beats = 12

b1 >> bass([0]*beats+[2]*beats+[3]*beats+[0]*beats,dur=PDur(beats,16,1),amp=PRand(P[1,0.8,0.9]*1.3))

Group(b1,k1).solo()

Group(a1,d1).play()

sorted(Player().get_attributes())

a1.solo()
d1 >> play('{-----[--][---]}')

from FoxDot.lib.Custom.Fractal import Fractal
Fractal().draw(0, 0)

print(Samples)

f1 >> pads([0,0,0,1], dur=8, sus=8)

f2 >> pads(f1.degree + 0.1, dur=8, oct=6, sus=8)

k1 >> play(PEuclid(3,8))

print(PEuclid(3,8,'-','X'))
d1 >> play(" -O-", sample=2, amp=0.2)

b1 >> saw(PRand([f1.degree]*3, PRand(P[0,1,2,3]+f1.degree)), amp=P[0,1,1,1, 0.5,1,0,1, 0,1,0.5,0, 0.5,0,1,1]*1.4, dur=0.25, su=0.5, oct=3, lpf=linvar([1000, 2000], 8), lpr=0.2)

b1 >> saw(PRand([0,1,2,3,4,5,6,7]), amp=P[0,1,1,1, 0.5,1,0,1, 0,1,0.5,0, 0.5,0,1,1]*1.4, dur=0.25, su=0.5, oct=3, lpf=linvar([1000, 2000], 8), lpr=0.2)

b2 >> pulse(b1.degree, dur=b1.dur, oct=b1.oct, lpf=1000, lpr=0.7)

Group(b1,b2).amplify = expvar([0,1], 1)

Group(b1,b2).solo()

Group(k1).amplify = var([1,0],[28,4])


print(SynthDefs)

print(dir(Scale))
