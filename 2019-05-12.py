FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

p1 >> pads()
p1.stop()
SynthDefs

p1 >> pads([0,2,[4,5]])

p1 >> pads([0,1,2,3], dist=1, hpf=PWhite(100,1000), hpr=0.4, dur=[1,.5,.5], amp=[0.7,.5], sus=2, pan=[-1,1], oct=P[3,4,5,4,6].shuffle().palindrome()).stop()
d1 >> play("*-o{-[-----]}", hpf=PWhite(100,1000), amp=1.5, hpr=0.2, sample=[0,1,1,3], dur=[3/4,3/4,1/2], pan=[-1,1], rate=P[1,2,.5,.2,-1,-2].shuffle().palindrome().palindrome())
d2 >> play("X[  ]X[  ]", amp=1.0, sample=2).often("stutter", PRand([2,3,5]), hpf=400, shape=0.5, dist=0.5, dur=2, hpr=0.1, pan=PRand([1,-1]))
b1.reset() >> sawbass(P[0,-1,3].palindrome().shuffle().palindrome(), dur=PDur(5,8), oct=P[6,5,5,5, 5,5,5,5], sus=0.2)
b1.reset() >> bass([0,-1,3], dur=8, shape=(0,[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]), chop=16, room=0.5, mix=0.2, amp=1.3)

p2 >> star(b1.pitch + (0,2,4), dur=[3/4,3/4,1/2]).every(6, "reverse").every(8, "shuffle").every(3, "offadd", 7)
p3 >> pluck(b1.degree + [0,4], dur=4, chop=320)
Group(b1,d1,d2,p3).solo()

Clock.clear()

help(Pattern)

p = P[1,2,3]
print(p.stretch(16)))

print(P[:4] & P[9,11])
print(p.shuffle().palindrome().palindrome())

p1.reset() >> blip(P[:10:2][:8].rotate(-3), dur=P[1,.5], sus=2)
p1.reset() >> blip(P[:10:2][:7].rotate(-3).shuffle().palindrome() + PStep(7,[0,3]).rotate() | P[[9,11]], dur=PDur(4,7), sus=2, pan=PSine(14).shuffle())
d1.reset() >> play("Xs", dur=.5, pan=P*(0,1), rate=P*(1,-1))
b1 >> dbass(var.chords,dur=PDur(PStep(3,4,3),7), amp=0.5, oct=[5,5,[6,4],5], pan=[0,[-1,1]]).every(3, "offadd", 4) + [0,0,4,0,7]
var.chords = var([0,-1,3], dur=[4,4,8])
d2.reset() >> play("  H ", dur=PDur(4,7))

p2.reset() >> pads(P^(0, 2, 4, 6), sus=2, dur=4)
p1.reset() >> pluck([P*(0, 3), P^(0, 2, 4, 0.75)], dur=2)
p1.reset() >> pluck([[0, P*(0, 0)], 2, -3, 2], dur=PDur(P[5,4,3,2],8))


d1.reset() >> play("xs", sample=2)
d2.reset() >> play("  * ", sample=2)
d3.reset() >> play("(+  )+( [( +)+])", sample=2)
d1 >> play("<xs><  * ><(+  )+( [( +)+])>", sample=2)
d1 >> play("<xs><  * ><(+  )+( [( +)+])>", sample=P(2, 0, 0), pan=P(0, 0, [-1, 1]))
d1 >> play("<|x2|s><  |*(3[33])| ><(h  )+( [( +)+])>", pan=P(0, 0, [-1,1]))
Clock.clear()

b1.reset() >> sawbass(var([7], 8), dur=1)
b1.reset() >> sawbass(var([0, 2], 8), dur=p1.dur, sus=0.3)
p1.reset() >> keys(b1.pitch + (0, 2, 4), dur=8)
p2.reset() >> blip(P[0, 2, 4].stretch(8), dur=1/2, sus=2) + var([0, 2], [6, 2])
d1.reset() >> play("<xs><  * ><(h  )h( [( h)h])>", sample=2)
