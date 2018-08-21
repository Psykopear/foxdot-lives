FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Scale.default=Scale.locrian

Root.default=var(P[0], 1)
m = Master()
m.hpf=0

s1 >> klank((b1.degree,b1.degree+P[5,3,1,1]), dur=2, hpf=sinvar([1000,4000],16), formant=sinvar([0,1],16), shape=(sinvar([0,1],16))).stop()
d1 >> play("-", sample=PRand(list(range(5))), dur=0.25, pan=PWhite(-0.8,0.8), amp=PEuclid(13,16)*PWhite(0.8,1.2))
k1 >> play("Xh", sample=2, hpf=0, hpr=0.2, amp=1)
d2 >> play("(h{--[--]}) (h )O(= -)", amp=0.7, mix=0.3, room=0.3)
b1 >> evilbass(var([0,0,1,0],8), dur=PRand([0.25,0.5]), amp=1.3, sus=0.4)
b1.stop()


group  = Group(s1,k1,b1)
group.hpf=1700;group.hpr=0.3;group.mix=0.4;group.room=0.4

Clock.bpm=134


d2 >> play("-", dur=1/3, echo=(0,0.2), mix=(0,0.6), room=(0,0.6), formant=(sinvar([1,0],16), PWhite(0,1))).stop()
(
    b2 >> evilbass(s3.degree, dur=2/4, sus=0.4, amp=PEuclid(P[9,8,7,6],12)*1.2),
    s3 >> pluck(var([0,1],8), dur=PRand([1/4,2/4]), amp=1.2),
    s4 >> ambi((s3.degree, s3.degree + 4), chop=2, shape=(0,0.5), formant=(0.5,0)),
    k3 >> play("X ", dur=1/4, sample=2, shape=(0,0.2)).every(16, 'stutter', PRand([2,1])),
)
m.hpf=0;m.hpr=0.3;m.mix=0;m.room=0;m.formant=0;m.shape=0,

Group(b2,k2).amplify=var([1,0],[28,4])

Group(k2,b2).solo()

m = Master()


m.hpf=800;m.hpr=0.3;m.mix=0;m.room=0;m.formant=sinvar([0,1],16);m.shape=sinvar([0,0.5],16)


Clock.bpm=180

Root.default=var([0,0],16)

s1 >> pluck(var([0,0,0,1],8), dur=1/4, sus=0.2, amp=PEuclid(11,16))
s2 >> ambi((s1.degree, s1.degree + 2), dur=4, chop=(8), formant=sinvar([0,1],16))
d1 >> play("-=h(i )", dur=1/2, amp=PEuclid(1,2)*PWhite(0.8,1), pan=PWhite(-0.80.8))
b1 >> evilbass(s1.degree, dur=PRand([1/3]), sus=0.5, lpf=0, lpr=0.9, dist=(0,0.2))
k1 >> play("X--",dur=5/7, sample=4, shape=(0,0.3), amp=1.5).every(PRand([8,4]), 'stutter', PRand([1,2,4]))

f1 >> fuzz(s1.degree, chop=4, amp=1, shape=(0,0.4))

d2 >> play("Vidhn", echo=0.1, hpf=PWhite(200,4000), hpr=0.3, dur=0.25, mix=0.4, room=0.4)

Group(k1,b1).amplify=var([1,0], [28,4])
Group(b1,s1,s2).solo()
s2.stop()
