from FoxDot import *

Scale.default=Scale.phrygian
Root.default=var([0, 5, 0], [12, 2, 2])
Clock.tempo=Fraction(4,4)

s0 >> klank(var([0, 2, 0, 0, 1, 0, 0, 3], [2]), chop=2, oct=(6), room=0.3, echo=0.1, mix=0.2, hpf=linvar([100, 2000], 16), hpr=0.2)
s2 >> sitar(s1.degree, shape=0.0, oct=(5), formant=(0.4,0.2), dur=(0.25), amp=PEuclid(8,16)*2, sus=0.1)
b1 >> evilbass(s1.degree, oct=5, dur=0.25, amp=PEuclid(7,16)*5, sus=0.4, cutoff=1900, rq=0.2)
k1 >> play("<X-X X-X X( t)>< (h ) o( h)>", hpf=0, hpr=0.2, sample=2, amp=(4.8, 1.2)).every(8, 'stutter', 2)


dnb = Group(k1,b1)

dnb.hpf=0;dnb.hpr=0.3;dnb.shape=(0);Master().amplify=var([1,1],[0.5,0.25])


Clock.bpm=140


d1 >> play(P["<er ( u) ><=(h )(- )( -)>"].amen(), sample=PRand([4,5]), dur=0.5, chop=(4,0), formant=(0, PWhite(0,0.9)))
k1 >> play("x-", sample=5)
s1 >> pluck(sus=0.2, dur=0.25, amp=PEuclid(9,15))
b1 >> sawbass(delay=0.5, amp=PEuclid(1,4)*8, dur=0.25, sus=0.2, cutoff=1900)
