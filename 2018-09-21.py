FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

d1 >> play("<|X2|:><|:2|  * >").every(6, 'stutter', 4, dur=3)
k2 >> play("Xh", sample=2, shape=(0,0.2), amp=2).sometimes('stutter', 4, dur=3)
k1 >> varsaw(dur=8, chop=64, delay=0, room=1, shape=0.5, oct=4, mix=0.3, amp=0.5) + (var([0,-1,-2],8),6,9)
p1 >> pluck((0,2,4,6), dur=PDur(3,8)*2, sus=2, amp=0.5)
b1 >> sawbass(var([0,4,[3,5]],8), dur=PDur(3,8,[0,2]), lpf=500, cutoff=sinvar([1000,7000],32), amp=1.4).often('offadd', 7)

Group(b1, k1, d1).solo()

p1 >> saw(P[:8], dur=1/4, vib=12, pan=sinvar([-1,1],4), drive=0.5, amp=PRand([0,1])[:16]).penta().every(6, 'splice', [7,6])

p1 >> pluck((0,2,4,const(6),const(9)), dur=PDur(3,8)*(1,2), sus=2, amp=0.5)

p3 >> space([0,7,3,4], dur=2).spread()
d1 >> play("|X2|:*-").sometimes('stutter', 4, dur=3).spread()
k1 >> play("|x5| ", dist=(0,0.2))
b1 >> evilbass(PRand([0,0,0,0,1,3,4]), oct=5, amp=PEuclid(11,16)*1.5, sus=0.4, dur=1/4).spread()
d2.reset() >> play("-", sample=PRand(list(range(5))), pan=PWhite(-1,1), delay=PRand([0,0.01,0.01,0.02,-0.01,-0.02,0,0])).spread()


p1 >> keys(P[:8])
(
p2 >> blip(p1.degree.map({
    lambda x: x >= 4:
    lambda y: y + (0,2),
    lambda x: x < 4:
    lambda y: y + P*(2,4,6)}
), scale=Scale.phrygian).stop(),
)

b1 >> sawbass(var([0,2,3,4]), cut=1/2).offbeat()
k1 >> play("X ")


s1 >> sitar() + (0,9)
# Circle of fifths!!
Root.default=var((PIndex()*4)%7,32)
