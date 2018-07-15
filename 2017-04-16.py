from FoxDot import *

# GIRI
plena = var([-5,0,-5,0,-5,0,-5,0, 0,-5,-5,0,0,-5,-5,0],[4])

# REGGAE
chord = (0,4,11)
tempo = var(P[0,-4,3,4],[8])
Scale.lydian


s1 >> viola(chord, scale=Scale.chromatic, dur=PRand([2]), amp=0.4).strum(PRand([0.04, 0.08, 0.06, 0.05]))
s2 >> viola(P[0,PRand([0,0,0,0,1,2,3,4])], scale=P[0,2,6,7,11], dur=PRand([.5]), oct=6, sus=0.5, amp=PEuclid(7,16)*0.4).strum(PRand([0.04, 0.08, 0.06, 0.05]))

m1 >> midi()

d1 >> play("-   ")
Synthdefs

Clock.bpm=120
Scale.default=Scale.minorPentatonic
Root.default = tempo

Root

d1 >> play("h", dur=1/3*2, chop=0, echo=0, mix=0.4, room=0.3)
d2 >> play("h", sample=1, dur=1/3, chop=0, echo=0, amp=PEuclid(6,9))
d3 >> play("t", hpf=PWhite(300,3000), hpr=0.2, dur=Fraction(1,3), chop=3, amp=PEuclid(7,12))
k1 >> play("x ( [  ] )", dur=1/3, sample=2)

k2.stop()
b1 >> bass(amp=PRand([0,1,1,1,1])*0.4, sus=0.3, dur=.5, shape=(0))


Group(b1,d1).solo()

w2 >> pluck(room=0.2, mix=0.2, formant=0.3, sus=0.3)
s1 >> klank(P[6,0,0,2, 1,0,4,0, 3,0,0,0, 3,2,1,0], dur=0.5, chop=1, formant=(0,PWhite(0.2,0.4)), room=0.3, mix=0.4, shape=0.2, hpf=PWhite(100,1000), hpr=0.3, amp=0.4).stop()
d2 >> play("{---=-}", sample=PRand(list(range(5))), dur=0.25, pan=PWhite(-0.8,0.8), amp=PRand([0,0.4,0.7,1]))
d1 >> play("<(=-)-(-[-])(-=)><(h) (o ) ><X >", chop=(4,0), room=0.3, mix=0.0, hpf=0).every(8, 'stutter', 0)
k2.reset() >> play("<x(-[--])><  o >", sample=3, amp=(1,0.5))#, echo=0.2, room=0.4, mix=0.2, shape=0.2)
b1 >> evilbass(P[1,0,2,0, 3,0,4,0, 4,0,4,0, 4,0,4,0, 4,0,3,0, 2,0,1,0, 4,4,4,4, 4,4,4,4]-4, dur=PRand([.25]), amp=PEuclid(4,8)*0.5, sus=0.8, cutoff=900, rq=0.3, oct=5, hpf=0)


Group(b1,d1,s1).stop()
