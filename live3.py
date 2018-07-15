from FoxDot import *

Root.default=var([8,8,8,4,4],[9,11,9,12,11])

Clock.bpm=130

Clock.clear()


t1 >> arpy()
t1.scale=Scale.chromatic
t1.degree=P[0,(0,12,16),(0,12,16),0,(12,15), 0,(0,12,15),(0,12,15),0,(12,16)]
t1.amp=[1,1,1,1,1, 0,1,1,1,1]
t1.dur=[.5,.5,.5,.25,.25]
t1.sus=0.4
t1.room=0.4
t1.mix=0.3


d1 >> play("o - -")
d1.room=0.8
d1.mix=0.4


Group(d1, k1).amplify=var([1,0],[28,4])


k1 >> play("V ", amp=0.5)

b1 >> bass()
b1.amp=P[0,1,1,1, 0,1,0.5,1, 0,1,1,0.5, 0.5,1,1,0]
b1.scale=Scale.phrygian
b1.degree=P[PRand([0,1,2,3,5]), 0, PRand([0,1,3]), 0]
b1.dur=Fraction(1,4)
b1.sus=0.2
b1.formant=linvar([0,3])

t1.solo()
