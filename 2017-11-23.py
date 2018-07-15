from FoxDot import *


Root.default = var([0,2,5,3,2],[8,8,8,4,4])
Root.default=0

s1 >> pluck()
s1.dur = Fraction(1,4)
s1.scale=Scale.phrygian
s1.degree=P[1,0,0, 3,0,0, 4,0,0, 2,0,0]
s1.sus=0.5
s1.amp=P[0,1,1,0.8, 0.,0.7,0.8,1, 1,0.,1,0.7, 0.,0.6,1,1]
s1.room=1
s1.mix=0.2


s2 >> klank(0, oct=4, hpf=linvar([100,10000]), amp=1.9)

s3 >> varsaw(PRand([0,7,2,4]), dur=4, bpf=3000, cut=2, stutter=4, chop=16, room=0.8, mix=0.3, amp=1.8)
s3.scale=Scale.phrygian


b1 >> sitar()
b1.degree=P[0,0,0,PRand([0,0,0,0,1,2,3,4])]
b1.scale=Scale.phrygian
b1.oct=(4)
b1.amp=PRand(P[1,1,1,1,0,0.7]*1)#P[0,1,1,1, 0.5,1,0,1, 0,1,1,0, 0,1,1,0.5]*1.0
b1.dur = Fraction(1,4)
b1.sus=0.2
b1.formant=0.0

Group(b1,s2,s3).solo()


d1 >> play("<X ><[--] {-[--]}>", sample=(4,PRand([0,1,2,3,4])), amp=(2,PWhite(0.8,1.3))).every(PRand([4,8,16]), 'stutter', 2)
d1 >> play("<X >", sample=(4), amp=(2).every(PRand([4,8,16]), 'stutter', 2)
d2 >>play("( {O[Oo][oo]}) ", room=1, mix=0.3, amp=0.5).every(2, 'stutter', 1)


Group(b1,d1).hpf=linvar([450,2000],4)
Group(b1,d1).hpr=0.2


Group(d1,d2).amplify=var([1,0],[28,4])


Master().hpf=0
Master().room=1
Master().mix=0.4


d1 >> play("X ", amp=0, sample=5)
b1 >> bass(P[0,0,PRand([7,9,1,2,3,4,0,0,0])], scale=Scale.minorPentatonic, amp=P[0.3,0.5,0.9,1], dur=0.25, oct=(6,5), sus=0.2)
b2 >> sitar(b1.degree, oct=4, amp=b1.amp, dur=0.25, lpf=400)
s1 >> pluck(PRand([0,2,4]), scale=Scale.minorPentatonic, chop=2, amp=PRand([0,0.4,1]))
d2 >> play("-  - [--] {--[--]}", amp=PWhite(1,2))
d3 >> play("o   ", mix=0.3, room=0.8)


print(SynthDefs)
