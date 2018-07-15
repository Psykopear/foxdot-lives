from FoxDot import *

d1 >> play(P["(h)(-h)o-"].amen(), sample=1)
d2 >> play(P["-"].amen().palindrome(), dur=P[1/2,1,1/2]).degrade()
d3 >> play("-",amp=2, dur=1/2).every(8, 'offbeat', 1).degrade()
k1 >> play("  ", sample=2, shape=(0.3,0.2), echo=(0.1,0.2), hpf=(300), hpr=0.3, amp=(1,0.8))
k2 >> play("V ", sample=2, amp=1)

Scale.default = Scale.minorPentatonic
b1 >> evilbass(P[0,2,3,4].stutter(P[4,2,2,2]), oct=4, dur=1).strum()
p1 >> pluck(dur=P[rest(1/2), 1/2]).follow(b1).strum(PRand([1/16,1/32])) + (0,1,3)
s1 >> pads(P[0,2,1,0,-1] + [1,3,4], formant=0.2, amp=0.2).follow(b1) + (0,2,4)

p1 >> pluck(PTri(5), scale=Scale.default.pentatonic)

help(pluck)

Scale.default=Scale.aeolian

ael = P[Scale.aeolian]

Root.default=var(ael[:3].shuffle().duplicate(2).mirror(), 1)
b1 >> evilbass(0, dur=0.5, amp=PEuclid(P[9,7,5,11].mirror().shuffle(),16)*2, oct=4, sus=0.6, cutoff=9300)
SynthDefs
b1 >> prophet(chop=3, oct=(5), amp=4)
b2 >> evilbass(0, dur=1, amp=PEuclid(5,8), oct=5, sus=0.6, cutoff=4000)
s1 >> sitar(dur=0.5, amp=PEuclid(P[9,11,20,23,15],32))
k1.reset() >> play("x-", sample=5, amp=2).every(32, "amen").every(PRand([4,8,16]), "stutter", PRand([2,1]))
d1 >> play(P["-( -)O(- )"].amen(), sample=2)
Clock.bpm=173
