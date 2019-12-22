from FoxDot import *

Scale.default=Scale.major
Clock.bpm=160

s1 >> pluck(b1.degree, dur=PDur(P[5],11), sus=1, oct=(4,5), room=0.5, mix=((0,0.5),(0,0.5)))
b1 >> evilbass(var([0,1,-1,1], [16,8,4,4]), oct=4, sus=0.5, dur=PDur(5,8), amp=1)
k1 >> play("X ", sample=2, amp=4, hpf=0).sometimes("stutter", 3, dur=1, hpf=400, hpr=0.1)
d1 >> play("h--*", amp=2, dur=PDur(5,11), echo=(0), sample=2).sometimes("amen")
s2 >> noise(hpf=sinvar([9000,200],32), hpr=0.2, formant=0.7, room=0.9, mix=(0,0.9))

Clock.clear()


s1.reset() >> space(oct=(4,5), dur=4, sus=4).stop()

s1.reset() >> quin(oct=5, dur=1, sus=1)

s1.reset() >> karp(oct=(4,5), dur=1, sus=1)

s1.reset() >> orient(var([0,2,4,6,7,6,4,2],[1]), oct=5, dur=1, sus=1)

s1.reset() >> space(var([0,2,4,6,7,6,4,2],[1]), oct=5, dur=1, sus=1)

b1.reset() >> dab((0,7), dur=16, sus=16, amp=0.3)

s2.reset() >> soprano(var([(9,13),(0,7),(2,9),(0,7),(1,8),(2,9)],32), oct=P[5,4], lpr=0.2, lpf=sinvar([100,5000],64), dur=16, sus=16, amp=1)

s3.reset() >> creep(s2.degree, dur=16, sus=16, amp=1, chop=64, pan=sinvar([-1,1],1/8))

SynthDefs


d1 >> play("h * u = ", sample=2, echo=0.06, rate=PRand([1,1,1,1,-1,.2,-2]), formant=PRand([0,0.1,0.2,0.3,0.4,0.5,0.6]), chop=4).spread()

b1.reset() >> evilbass(s2.degree, dur=PDur(P[3,4,5],8), oct=(4), sus=0.9, amp=0.7, lpr=0.2, lpf=400)
k1 >> play("<X ><h-*n[--]l>", sample=2, amp=4.5)

