from FoxDot import *

sawbass = FileSynthDef('sawbass')

DefaultServer.loadSynthDef('/home/docler/Github/FoxDot/FoxDot/osc/scsyndef/sawbass.scd')

Clock.bpm=140

Root.default=var([0,2,0,3,2,2],[8,8,8,4,2,2])

b1 >> sawbass(P[0,PRand([1,2,3,4,5,6,7]),0], cutoff=expvar([400, 1900], 0.25), rq=0.2, oct=3, sus=0.01, dur=Fraction(1,4), scale=Scale.phrygian, amp=PEuclid2(4,11,0.5,1)*0.2, formant=0.0, shape=0, hpf=0, hpr=0.2)

k1 >> play("<X[( -)(- )]>", sample=2, amp=1, chop=0, room=0.8, mix=0.1)
d1 >> play("<(=   ){n[--][n-]}>", sample=3, chop=2, amp=2).every(8, 'stutter', 2)
d2 >> play("<(o   )><(x  [xx] )>", chop=3, sample=3, shape=0.9, hpf=linvar([500, 3000]), hpr=0.3, formant=expvar([0,9]), dur=0.5, amp=0.7, room=0.7, mix=0.2)
d3 >> play("(  O)", amp=0.4)

k1.stop()
d1.stop()
d2.stop()

Group(k1,d1,d2).amplify=var([1,0],[28,4])
Group(d1,d2).room=0.5
Group(d1,d2).mix=0.2

Group(b1,k1).solo()
b1.solo()



# New synth!
# I need to fix some default paramts
s1 >> sawbass(P[0,PRand([0,1,2,3,4,5]),0], scale=Scale.phrygian, rq=0.1, oct=(3), cutoff=linvar([400, 2000], 0.5), amp=PRand([0,1,1,0.7])*0.2, sus=0.001, dur=Fraction(1,4))

s2  >> varsaw(s1.degree, scale=Scale.phrygian, oct=6, dur=0.25, chop=4, bpf=linvar([400,4000]), bpr=1, pan=(PWhite(-1,0), PWhite(0,1)), shape=(0.8,0.7))
s2.stop()

k2 >> play("V-")
k2.stop()
k2 >> play("<V ><[  ]>", amp=1, hpf=0)
d1 >> play("<(o n)><(n  )(-- [--])>", hpf=linvar([100,2000],16), hpr=0.1, formant=linvar([0,1],8), shape=0.1, room=0.7, mix=0.2)
d2 >> play("<=   ><O   ><{-[--] }>", amp=(1,0.3,1))
