from FoxDot import *

Root.default=var([9,11,9,12,11], [8,8,8,4,4])

t1 >> arpy()
t1.scale=Scale.chromatic
t1.degree=P[0,(0,12,16),(0,12,16),0,(12,15), 0,(0,12,15),(0,12,15),0,(12,16)]
t1.dur=P[.5,.5,.5,.25,.25]
t1.amp=P[1,1,1,1,1, 0,1,1,1,1]
t1.room=0.7
t1.mix=0.3

d2 >> play("x  {x } ")
d1 >> play("o - -")

d1 >> play("{ -[--]}", dur=0.5)
d1.sample=PRand([1,2,3,4,0])




b1 >> bass(oct=4)
b1.dur=Fraction(1,4)
b1.amp=P[0,1,1,1, 0.5,1,1,0, 0,1,0,1, 1,0.5,1,1]
b1.scale=Scale.phrygian
b1.degree=P[PRand([0,1,2,3,5]),0,0]
b1.sus=0.3
b1.formant=0
b1.hpr=0.1
b1.hpf=500


Group(d1,d2).amplify=var([1,0],[28,4])
