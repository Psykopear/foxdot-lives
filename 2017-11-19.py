from FoxDot import *

Root.default=var([9,11,9,12,11],[8,8,8,4,4])

t1 >> arpy()
t1.scale=Scale.chromatic
t1.degree=P[0,(0,12,16),(0,12,16),0,(12,15), 0,(0,12,15),(0,12,15),0,(0,12,16)]
t1.dur=P[.5,.5,.5,.25,.25]
t1.amp=P[1,1,1,1,1, 0,1,1,1,1]*1.4
t1.sus=0.5
t1.room=0.4
t1.mix=0.2


# drumssss
d1 >> play()
d1.degree="o - -"
d1.room=0.5
d1.mix=0.2

#other drums first
d2 >> play("")
d2.degree="{ -[--]}"
d2.sample=PRand([0,1,2,3,4])
d2.pan=PWhite(-0.5,0.5)
d2.amp=PWhite(0.8,1.3)

Group(d1,d2).amplify=var([1,0],[28,4])


# Kickkk
d3 >> play("")
d3.sample=2
d3.degree="V "


#Bass

b1 >> bass()
b1.scale=Scale.phrygian
b1.degree=P[PRand([1,2,3,5]),0,PRand([1,3,4]),0]
b1.amp=P[0,1,1,1, 0.5,1,0,1, 0,1,1,0.5, 0,1,0.5,1]*0.7
b1.hpf=500
b1.oct=(4,5)
b1.dur=Fraction(1,4)
b1.sus=0.3
b1.formant=0.5

# Bass bass
b2 >> saw(b1.degree, oct=3, amp=b1.amp*2, dur=b1.dur, sus=0.4, lpf=500, lpr=0.2)


Group(b1,b2).hpf=4000


Clock.clear()
