FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0,3,0,5], 8)
m = Master()

bass_1 = {
    'dur': P[1,1,1,.5,.5]/2, 
    'sus': 0.4, 
    'degree': [0,3,1,3,0]*2 + [0,5,0,3,0]*2, 
    'scale': Scale.chromatic
}
b1 >> evilbass(**bass_1, amp=0.5, oct=(3,4))
s1 >> pluck(**{**bass_1, 'dur':PDur(P[3,4],8)}, oct=(4,5), delay=(PRand([0,.25]),0.25))
d1 >> play("h-o(-[--])", hpf=PWhite(100,500), hpr=0.2, echo=(0,0.1), amp=(2,0.4), mix=(0.3,0.6), room=0.4).sometimes("amen")
k1 >> play(P["x x x x [xx] [xx] [xx] [xx] "].shuffle().mirror(), hpr=0.2, hpf=PWhite(200,2000), sample=2).sometimes('stutter', 4, dur=3)
k2 >> play(P["x "], sample=4, hpf=0, hpr=0.2, amp=1.5).sometimes('stutter', 2, dur=3)

a1 >> audioin(room=0.9, mix=(0.0,0.9))
d1 >> play("x-(-x)-", dur=0.5).sometimes('amen')
b1 >> evilbass(oct=4, amp=0.3, dur=0.25, sus=0.3)
