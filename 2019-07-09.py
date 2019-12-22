from FoxDot import *

Scale.default=Scale.major


Clock.bpm=160

SynthDefs

s1.reset() >> pluck(P[0,2,4,6,7,6,4,2], amp=2, dur=.5, oct=(4,5), sus=P[.5,.25,1].stutter(6).shuffle(), room=0.6, mix=(0,0.5), pan=PWhite(-1,1)).spread()

b1 >> sawbass(s1.degree - 7,sus=0.2,  chop=(0), formant=(0,P[0,0.1,0.2,0.3,0.4,0.5]), dur=PDur(P[3,5,4,3,4,5].shuffle(),8))
k1 >> play("docler  ", echo=(0,0.1), amp=0.2, chop=4, rate=P[1,1,1,-1,.2].stutter(2).shuffle().palindrome(), sample=2).sometimes("amen")
k2 >> play("X ", sample=2, shape=(0,0.4,0.9), room=0.6, mix=(0,0.6), hpr=0.3, hpf=(0,300)).sometimes("stutter", 3, dur=1)

s1 >> pluck(P[0,2,4,6,7,6,4,2], dur=.5, sus=PRand([.25,.25,.25,.5]), oct=PRand([4,5]), room=0.8, mix=(0,0.5)).spread().sometimes("amen")


b1.spread()
b1.lpf=sinvar([200,3000],32)


b1 >> sawbass((9,13), dur=16)

b1 >> sawbass((0,7), dur=16)

b1 >> sawbass((2,9), dur=16)

b1 >> sawbass((0,7), dur=16)

b1 >> sawbass((1,8), dur=16)

b1 >> sawbass((2,9), dur=16)

b1 >> evilbass(sus=1.5, dur=PDur(P[3,2,4,3,3].shuffle(),8), amp=.5,room=0.4, mix=(0,1), oct=(4)).follow(s1)

b1 >> evilbass(s1.degree, sus=0.45, dur=PDur(P[3,4,5],8), amp=P[0.2,0.7,0.8,1]*0.6, oct=(4))
k1 >> play("h*-t", echo=0.08, hpr=0.2, hpf=0, sample=2).sometimes("stutter", 3, dur=2, hpf=1400, hpr=0.2).sometimes("amen")
k2 >> play("X[xx]", shape=(0,0.1), room=0.4, mix=(0,0.5), sample=2, amp=1.5)

Clock.clear()
