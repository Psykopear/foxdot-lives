from FoxDot import *

Scale.default=Scale.phrygian

Clock.bpm=83

k1 >> play("X[  ]", sample=2, hpf=0).sometimes("stutter", 4, dur=1, hpf=200)
d1 >> play("{[  ] }",sample=0,  echo=0.1, mix=0.3, room=0.3, formant=sinvar([0,1.4],8), amp=0.9).sometimes("amen")
b1 >> evilbass(var([1,0,0,0,0],[8,8,8,6,2]), dur=PDur(P[8],8), sus=0.4, hpf=0, oct=(4), amp=expvar([0,1],0.5))

n1 >> noise(hpf=sinvar([400,1000], 16), hpr=0.4, formant=PWhite(0,1), dur=0.25, amp=1)

d2 >> play("rh**", dur=0.25, echo=(0,0.1), mix=(0.2,0.8), amp=(1,0.5), dist=sinvar([0,0.5],16), formant=1)

s1 >> pluck((b1.degree, b1.degree + 2), chop=2, dur=PDur(P[5,6,7,6],8), dist=0.2, sus=0.6, formant=(0,0.4), oct=((4,5),5), amp=0.0)


g = Master()


m.hpf=0;m.hpr=0.2;m.room=0;m.mix=0;

b1.reset() >> evilbass(var([0,1,2,3,-1],[8,8,8,6,2]), dur=PDur(P[9],16), delay=0, sus=0.4, hpf=0, oct=(4), amp=0.0)

s1.reset() >> prophet((b1.degree, b1.degree + 2) + PRand([0,0,0,0,2,-2]), chop=16, pan=PWhite(-1,1), dur=2, amp=0.8, shape=(0,0.5), ).spread().stop()

d1.reset() >> play(" ", dur=PDur(9,16).shuffle(), sample=PRand(list(range(5))), amp=0.8, pan=sinvar([-0.8,0.8],6)).spread()

k2.reset() >> play("X", sample=2, room=(0,0.8),mix=(0,0.8), hpf=(0,400), hpr=0.1, shape=(0,0.2), formant=(0,0.1), amp=2, dur=0.5)
b2.reset() >> evilbass(PRand([1,0,0,0]), dur=PDur(P[5],8), delay=0, sus=0.4, lpf=PWhite(500,1000), lpr=0.2, oct=(4,5))

k1 >> play("X", sample=2, room=(0,0.8),mix=(0,0.8), hpf=(0,400), hpr=0.1, shape=(0,0.2), formant=(0,0.1), amp=2, dur=0.5)
b1 >> evilbass(PRand([1,0,0,0]), dur=PDur(P[5],8), delay=0, sus=0.4, lpf=PWhite(500,1000), lpr=0.2, oct=(4,5))
m = Group(k1,b1)

g.hpf=0;g.hpr=0.2;g.lpf=800;g.amplify=0.0

Clock.clear()

s1.reset() >> sitar(b1.degree, dur=PDur(9,12).shuffle(), amp=1, sus=0.7, chop=0, pan=PWhite(-1,1), oct=P[4,5,7]).stop()

m.formant=sinvar([0,4],16, start=now)

