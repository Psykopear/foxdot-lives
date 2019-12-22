from FoxDot import *

Scale.default=Scale.phrygian
Clock.bpm=120
tempo = Player()
tempo >> play(amp=0)
tempo.dur=Fraction(1,3)
t = { 'dur': tempo.dur }

Clock.clear()

t
s1 >> sitar()


Scale.default=Scale.phrygian
Clock.bpm=120



s1 >> ambi(0, chop=3, amp=1)
d1 >> play("<x-->", **t, echo=0, hpf=0, hpr=0.2)
d2 >> play("(=h)-(o )(- )", hpf=PWhite(400, 4000), hpr=0.2, pan=PWhite(-0.8,0.8), **t)
s2.reset() >> viola(var(P[0,3,2,1], P[10,2,2,2]), sus=0.2, amp=1, **t)
s2 >> sitar(P[0, PRand([2,3,4,1])], amp=PEuclid(P[5,4,7,6,5].shuffle().mirror(),9), sus=0.1, **t)
b1 >> dbass(s2.degree, sus=0.2, amp=PEuclid(P[3,4,5,6,7,7,7].shuffle().mirror(), 9), **t)
#, hpf=PWhite(300, 4000), dur=0.25, hpr=0.3, shape=(0,0.2))

Group(k1,b1).solo()
Master().hpf=20000;Master().hpr=0.6;Master.room=0.4;Master.mix=0.3;
Master().formant=0;Master().shape=0;
b1.reset() >> sawbass(s2.degree, sus=0.2, dur=1/3, amp=PEuclid(12,12))
k1.reset() >> play(P["<X ><  O >"], sample=2, hpf=0, dur=Fraction(1,2), shape=(0,0.2), formant=(0,0.2)).every(8, 'stutter', 4)
b1 >> dbass(PRand([0,1,2,0,0]), dur=PRand(P[1,2]/3), sus=0.3)
s3 >> pluck(b1.degree, dur=Fraction(1/6), amp=PEuclid(9,12)*2)

s3 >> ()
a = iter(SynthDefs)
next(a)


k2 >> play(P["X({--- }{O[--]--O})"], sample=2, amp=1.0)
s3 >> eval(next(a))(amp=1.0)
Group(k2,s3).solo()


t1 >> ambi(0, dur=Fraction(1,2), amp=0)
metro = { 'dur': t1.dur, 'degree': t1.degree }


s1.reset() >> bug(3, oct=3)


b1.reset() >> varsaw(**metro)
c2 >> sitar(**metro)
# BUG!
# DBASS!
# DAB!
# VARSAW!
# GROWL? Low sus 0.4
# DIRT!
# VIOLA!
# FEEL?
# PLUCK! or SPARK
# BLIP
# RIPPLE!!
# ZAP, it is low volume
f1 >> pluck(dur=1, sus=0.3, oct=(4,5), dist=0.06, tremolo=0.4, spin=0.9, beat_dur=1/2, formant=1, shape=.4, chop=1, amp=1.6)
s3.oct=(5)
s3.chop=0
s3.mix=0.3
s3.room=0.3
s3.scale=Scale.aeolian
f1.degree=var([0,P[2,3,4,5].mirror(),P[1,2,1,3].mirror()],[8,4,4])
s3.degree=P[0,(0,12,16),(0,12,16),0,(12,15), 0,(0,12,15),(0,12,15),0,(12,16)]
s3.scale=Scale.chromatic
f1.amp=P[1,1,1,1,1, 0,1,1,1,1]*2
f1.dur=P[.5,.5,.5,.25,.25].amen()
s3.sus=(0.6)
