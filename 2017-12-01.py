from FoxDot import *

Scale.default.set("phrygian")
Root.default=var([4,4,6,3,3],[4,4,6,1,1])

# 19/8 bass where you can play with polyrithms with drums
b1 >> sawbass(P[5,0,0, 5,0,0, 6,0,5,0, 5,0,0, 5,0,0, 4,6,0], scale=Scale.chromatic, root=4, oct=(4,5), sus=0.2, dur=Fraction(1,2), cutoff=900, rq=0.2, amp=3)
# fake sidechain
b1 >> sawbass(P[5,0,0, 5,0,0, 6,0,5,0, 5,0,0, 5,0,0, 4,6,0], scale=Scale.chromatic, root=4, oct=(4,5), sus=0.2, dur=Fraction(1,2), cutoff=900, rq=0.2, amp=expvar([0.2, 3], 0.5))
b1 >> sawbass(P[2,0,0, 2,0,0, 3,0,2,0, 2,0,0, 2,0,0, 1,0,0], oct=(4,5), sus=0.2, dur=Fraction(1,2), cutoff=900, rq=0.2, amp=2, room=0.0, mix=0.0)
b1 >> sawbass(P[2,0,0, 2,0,0, 3,0,2,0, 2,0,0, 2,0,0, 1,0,0].palindrome().i_shuf(), oct=(4,5), sus=0.2, dur=Fraction(1,2), cutoff=(200, 900), rq=(1, 0.2), amp=3, room=0.0, mix=0.0)
b1.stop()

d1 >> play("<=       [nn]       ><X--X--X-X-X--X--X-X>", amp=1, delay=0, sample=2, dur=0.5, room=0, mix=0)
d1 >> play("<X ><-><Oo Oo OoO Oo Oo OOo>", amp=(1,3,0.7), delay=(0, PRand([0, 0.01, 0.02, -0.02, -0.01, 0, 0]), 0), dur=0.5, sample=(2,PRand([0,1,2,3]),1))
d2 >> play("-", dur=Fraction(1,4), amp=PRand([0,1,1,1]), delay=PRand([0, 0.01, 0.02, -0.02, -0.01, 0, 0]), sample=PRand(list(range(5))), pan=(PWhite(-1,1), PWhite(-1,1)))
d1 >> play("<  ><-><o  o  o o o  o  oo ><4   3   2   1   >")
d1 >> play("[--]-[---]-[--]")
d1 >> play("<X >< [--]>", amp=(1, 1), sample=(2, 1), dur=0.5, room=0.2, mix=0.1)

s1 >> varsaw(b1.degree, sus=0.2, chop=4, dur=0.25, oct=4, hpf=linvar([500, 2000], 16), hpr=0.2, amp=expvar([0.2, 2], 0.5))
c1 >> klank((b1.degree, b1.degree + 5), chop=8, amp=1, oct=5)

s3 >> arpy((b1.degree, b1.degree + 5), dur=Fraction(1,4), oct=6, shape=PWhite(0.3, 0.5), formant=0.4, amp=expvar([0, 2.5], 0.5), mix=0.2, room=0.4, hpr=0.4, hpf=PWhite(100, 2000))
s1.stop()
c1.stop()
s3.stop()


Master().lpf=0
Master().lpr=0.7
Master().mix=0.7
Master().room=0.3

print(SynthDefs)


b1 >> sawbass(P[2,0,0, 2,0,0, 3,0,2,0, 2,0,0, 2,0,0, 1,0,0].palindrome().i_shuf(), oct=(4,5), sus=0.2, dur=Fraction(1,2), cutoff=(200,900), rq=(1,0.2), amp=3, room=0.0, mix=0.0)
