from FoxDot import *

Clock.clear()

Scale.default=Scale.hungarianMinor

SynthDefs

s1 >> ambi(
        P[0,0,0,1,-1, 0,3,2,1,-1].stutter(P[4,4,4,2,2]).shuffle(),
        formant=b1.formant,
        oct=P[6,5,5,5],
        dur=0.25,
        sus=0.2,
        amp=0.1,
        shape=P[0,0,.1,.2,.3,.4,.5,.6].shuffle().palindrome()
        )
b1 >> jbass(s1.degree + PRand([0,0,0,1,2,3]), formant=(0, P[0.3,0.6,0.8,1,2,3,4,5,6,7,8].shuffle()), dur=PDur(P[3,5,4,5],8), sus=0.5, oct=(5,6), amp=0.9)
d1 >> play("<X><=>-<X><*>([--]-)", amp=1, sample=2, rate=(1,P[.2,-1,.3,-.5].shuffle()))
