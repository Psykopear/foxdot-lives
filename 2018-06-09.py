from FoxDot import *

Scale.default=Scale.aeolian

Clock.bpm=124

Clock.clear()


tempo = Player()
tempo >> pluck(amp=0)
tempo.dur=Fraction(1,3)
t = { 'dur': tempo.dur }


s1 >> klank([0] + P[0,0,3,2,1,1,-1].shuffle().mirror(), chop=8, sus=2, dur=2, vib=0.4, fm_saw=sinvar([1,1], dur=16))

s2 >> sitar(s1.degree, sus=0.1, oct=(4, 5), dur=Fraction(1,4), amp=PEuclid(P[5,8,6,12,12,9].shuffle().mirror(), 16)*0.6)

d1 >> play("(---o)", sample=PRand(list(range(5))), amp=PEuclid(P[4,5,6,7].mirror().shuffle(),8)*PWhite(0.4,1)*2, pan=PWhite(-0.8,0.8))

s3 >> growl((s1.degree + 2, s1.degree + 2), sus=0.4, dur=0.25, amp=PEuclid(5,8)*0.9, oct=(5,6))
b1 >> evilbass(s1.degree, sus=0.5, dur=0.25, amp=PEuclid(5,8)*0.5, oct=4)

k1 >> play("x ", sample=5, amp=2.5)

Group(d1,b1).amplify=var([2,0],[28,4])
Group(d1,b1).room=0.4
Group(d1,b1).mix=0.4

b1.stop()
