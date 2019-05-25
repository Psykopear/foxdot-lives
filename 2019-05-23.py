from FoxDot import *

Clock.clear()

Scale.default = Scale.justMinor


s1 >> ambi((s2.degree, s2.degree + 2) + (0.11,0,-0.05), shape=0.2, chop=P[2,4], amp=.3)

s2 >> pluck(P[2,0,-2,1,0,3].stutter(4).shuffle().palindrome() + (0.11,0,-0.05), oct=(4,5), amp=.2, sus=1.4, dur=PDur(P[2,[3,5]],8))

b1 >> evilbass(s2.degree, amp=0.4, dur=PDur(P[3,[5,2]],8), oct=P[4,5], sus=0.4)

k1 >> play("X-x*", sample=2, hpf=PWhite(400,1000), hpr=0.3, amp=.1, rate=PRand([1,-1,1,.2,-.5,-1]))

k2 >> play("X-", room=0.5, mix=(0,0.8), sample=2, dur=.5, hpf=0, amp=0.9)



s1 >> klank(P[0,1,-1,2,1].stutter(P[4,4,4,2,2]), chop=PRand([2,4]), dur=1, shape=PRand([.0,.1,.2,.3,.4,.5,.0,.0,.0]))
s2 >> pluck(s1.degree + (0, 2), dur=PDur(P[3,5,4,3],8), sus=0.3, hpf=PWhite(100,1000), hpr=0.1,)
d1 >> play("=-h-", sample=2, rate=PRand([1,1,-1,-.2,.3]), amp=1.55).sometimes("stutter", 3, dur=2, hpf=1500)
k1 >> play("X ", sample=1)
