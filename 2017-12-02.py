from FoxDot import *

Scale.default.set("phrygian")
Root.default = var([4,4,4,6],[4,4,4,4])

b1 >> sawbass(P[2,0,0, 2,0,0, 3,0,2,0, 2,0,0, 2,0,0, 1,0,0], oct=4, sus=0.2, cutoff=900, dur=0.5, amp=5)

d1 >> play("<=       [nn]       ><X--X--X-X-X--X--X-X>")
d1 >> play("<=       [nn]       >< -- -- - - -- -- - >")
d1 >> play("<V ><-><Oo OoO Oo Oo OOo>", amp=(1,1,0.6), delay=(0, PRand([0,0.01,-0.01,0.02,-0.02,0,0]),0), dur=0.5, sample=(2,PRand([0,1,2,3]),1))

d2 >> play("-", dur=0.25, amp=PRand([0,1,1,1]), delay=PRand([0,0.01,-0.01,0.02,-0.02,0,0]), sample=PRand(list(range(5))))



s1 >> varsaw(b1.degree, chop=4, shape=(0,0.2), sus=0.1, dur=0.125, oct=5, hpf=linvar([5000, 2000],16), hpr=0.1, amp=expvar([0,1.5],0.125))
s2 >> arpy((b1.degree, b1.degree + 5), dur=0.25, oct=6, shape=PWhite(0.3,0.5), formant=0.4, amp=expvar([0,2.5],0.5), mix=0.2, room=0.4, hpr=0.3, hpf=PWhite(100,2000))

Group(d1,d2).amplify=var([1,1],[8,4])
