FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.locrianMajor
Root.default=var(P[0], 1)
m = Master()

s1 >> prophet(var([0,3,-2,1], 8), chop=PRand([4,8]), oct=(4,5), hpr=0.2, hpf=sinvar([100,1000], 16)).spread()
s2 >> fuzz(s1.degree, amp=0.5, sus=0.2, dur=PRand([0.25, 0.5]) )
d1 >> play("-", dur=0.25, sample=PRand(list(range(1))), pan=PWhite(-1,1), amp=PWhite(0.8,1.2)*PRand([0,1])).stop()
d2 >> play("(    ) * ", room=0.4, mix=0.4, echo=(0,0.1)).spread()



Clock.bpm=126


Group(k1, b1).solo()
b1 >> evilbass(var([1,0,3,0,0], 8), dur=PDur(P[5,3],8)/2, oct=5, sus=0.4, amp=P[0,1,1,1])
k1.reset() >> play("<|X2|-><    >", sample=1, shape=(0), hpr=0.2, hpf=0, amp=(1.2,0.3))
d1.reset() >> play("h( -)o(- )", room=0.4, mix=0.4).spread().stop()
s1.reset() >> sitar(b1.degree, dur=PDur(3,8), amp=1.0, formant=sinvar([0,1],16)).stop()
s3 >> viola(b1.degree, oct=4, sus=4, dur=4, chop=P[4,8,16])
d2 >> play("alsdha", dur=0.25, echo=(0,0.1), mix=0.4, room=0.4, formant=sinvar([0.5,2],16), hpr=0.2, hpf=sinvar([100,2000],16), amp=0.6, chop=4).stop()
s4 >> pluck(b1.degree, delay=0.25, oct=(5,6), dur=PDur(P[9,3,11],16), chop=P[0,2,4], formant=(0,1,2)).spread().stop()

s5 >> razz(b1.degree, dur=0.5, amp=P[0,1], )
Group(s4,b1,k1).solo()
SynthDefs


Group(k1,b1).solo()
(
)
s1.reset() >> sitar(b1.degree, dur=PDur(4,6), shape=(0,0.2), oct=(4,5), chop=P[1,3], amp=PWhite(0.8,0.4)).stop()
b1.reset() >> evilbass(P[0,0,0,0, 0,0,0,0, 3,0,1,0, 0,0,1,0], dur=1/3, amp=P[0,1,1,1, 1,0,1,1, 0,0,1,1, 1,0,1,1]*0.7).stop()



s1.reset() >> klank(b1.degree + (0,3,5), dur=1, chop=4, formant=sinvar([0,1],16), shape=sinvar([0,0.3],16))
b2 >> bass(0, dur=PRand([0.25,0.5]), sus=0.3).stop()
k1.reset() >> play("<V ><|h2|->",dur=0.5,  echo=(0), shape=0, amp=1)
Master().hpf=10700;Master().hpr=0.4;Master().mix=0.3;Master().room=0.3;Master().formant=0.3
