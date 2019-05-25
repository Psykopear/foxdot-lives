from FoxDot import *

Scale.default=Scale.blues

Clock.bpm=134
Clock.clear()

Root.default=var([0,0,5,5,0,0,7,5], 8)

s1.reset() >> pasha(oct=4)
SynthDefs

s1 >> klank(var([0,1,2,-1], [8]), dur=0.5, chop=2, shape=P[.0,.1,.2,.3,.4,.5], pan=PWhite(-1,1))
d1 >> play("-h*[--]0", rate=PRand([1,.2,-1,2,.3,-2,1,1])).often("stutter", 3, dur=2, hpf=500, hpr=0.3)
d2 >> play(" ", dur=PDur(P[5,3,7,4],8), sample=PRand(list(range(6))), pan=PWhite(-1,1), hpf=PWhite(100,2000), hpr=0.3)
b1 >> evilbass(s1.degree + P[0,0,0,0,1,2], dur=PDur(P[7,5,4,3],8), sus=0.3, amp=0.5, oct=(4))


SynthDefs

k1 >> play("x-h-", sample=2, hpf=0, dur=.5, hpr=0.2).sometimes("stutter", 2, dur=3, hpf=400)
s1 >> pluck(P[0,0,0,1,2,3,-1,-2].stutter(3).shuffle().palindrome(), dur=PRand([1/3,2/3]), oct=(4,5,6), hpf=300, hpr=0.2).stop()
s2 >> noise(dur=.25, hpf=PWhite(100,4000), amp=.9, shape=P[0,.1,.2,.3,.4,.5], amp=1.2)
b1.reset() >> evilbass(P[0,0,0,1,2,3,-1,-2], dur=PDur(P[4,5,3],8), sus=0.4, amp=0.9, oct=(4), hpf=2000, hpr=0.2)
s3 >> sitar(b1.degree + PRand([0,0,0,0,1,2,3]), dur=PDur(3,8), chop=2, amp=.9, shape=(0,0.4))
