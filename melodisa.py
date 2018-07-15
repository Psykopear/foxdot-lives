from FoxDot import *

Clock.bpm=130

Clock.clear()

Scale.default.set("chromatic")


TrancePlucked = Player()
TrancePlucked >> arpy()
TrancePlucked.degree =  [0,(0,12,16),(12,16),0,(12,15), 0,(0,12,15),(12,15),0,(12,16)]
TrancePlucked.amp    = P[1,1,1,1,1, 0,1,1,1,1]*2
TrancePlucked.dur    = P[.5,.5,.5,.25,.25]
TrancePlucked.oct    = 5
TrancePlucked.sus    = 0.5
TrancePlucked.room   = 0.5
TrancePlucked.mix    = 0.3


Kicker = Player()
Kicker >> play()
Kicker.amp=1.5
Kicker.degree = "X "
Kicker.hpf=0
Kicker.sample=2
Kicker.stop()

Drummer = Player()
Drummer.degree="o -{-[--]} "
Drummer >> play()

Drums = Group(Drummer, Kicker)

Drums.amplify=1
Drums.amplify=var([1,0],[28,4])

Basser = Player()
Basser.scale=Scale.phrygian
Basser.degree = P[PRand([0,1,2,3,4]),0,PRand([0,1,2,3,4]),0]
Basser.dur = Fraction(1,4)
Basser.sus=0.2
Basser.oct=(5,6)
Basser.shape=0.1
Basser.lpf=linvar([1000, 2000], 4)
Basser.lpr=0.3
Basser.amp=[0,1,1,1, 0.5,1,0,1,  1,0.5,0,1, 1,1,0,1]

Basser >> bass()
Basser.solo()
Basser.every(14, 'stutter', 5)
Basser.formant=(0,2.)
dir(Basser)



print(dir(P[]))

m1 >> arpy(melody, amp=amp, oct=5, dur=durs, sus=0.4, room=1, mix=0.2)

print(SynthDefs)







p1 >> arpy()
p1.scale=Scale.chromatic
p1.degree=P[0,(0,12,16),(12,16),0,(0,12,15),  0,(0,12,15),(12,15),0,(0,12,16)]
p1.amp=P[1,1,1,1,1, 0,1,1,1,1]*2
p1.sus=0.4
p1.dur=P[.5,.5,.5,.25,.25]
p1.room=0.4
p1.mix=0.2


k1 >> play()
k1.degree="X[--]"

d1 >> play()
d1.degree="- - [--]"

d2 >> play()
d2.degree="o    "

# Ok let's bring in some bass

b1 >> bass()
b1.scale=Scale.phrygian
b1.degree=P[0,PRand([0,1,2,3,4,5]) ,0, PRand([0,1,3,4])]
b1.amp=0.3
b1.dur=Fraction(1,4)
b1.sus=0.3
b1.oct=(5,6)
b1.amp=P[0,1,1,0, 0.5,1,0,1, 0,1,0.5,1]*0.7
