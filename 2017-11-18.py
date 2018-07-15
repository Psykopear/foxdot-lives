from FoxDot import *

Root.default=var([9,12,9,15,12], [8,8,8,4,4])

Clock.bpm=128

t1 >> arpy()
t1.scale=Scale.chromatic
t1.degree=P[0,(0,12,16),(0,12,16),0,(12,15), 0,(0,12,15),(0,12,15),0,(12,16)]
t1.amp=P[1,1,1,1,1, 0,1,1,1,1]
t1.dur=P[.5,.5,.5,.25,.25]
t1.sus=0.4
t1.room=1.0
t1.mix=0.2
t1.hpf=linvar([1000,0],0.5)
t1.hpr=0.3
t1.every(2, 'stutter', 2)
t1.stutter=1


d1 >> play()
d1.degree="x "
d1.root=0
d1.amp=2
d1.sample=1
d1.room=0.2
d1.mix=0.2

d2 >> play()
d2.degree="{ -[--]}"
d2.sample=PRand([0,1,2,3,4])
d2.amp=PWhite(0.8,1.3)

b1 >> bass()
b1.oct=(4,5)
b1.amp=P[0,1,1,1, 0.5,0,1,1, 0,1,0.5,1, 0,1,1,0]*0.5
b1.dur=Fraction(1,4)
b1.sus=0.2
b1.shape=0.3
b1.lpf=var([1000,2000],8)
b1.lpr=0.2
b1.formant=PWhite(0,3)
