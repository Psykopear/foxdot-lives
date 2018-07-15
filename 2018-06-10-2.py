from FoxDot import *
Clock.clear()

Scale.default=Scale.choose

def drange(start, end, step=0.1):
    r = start
    while r <= end:
        yield r
        r += step


s1 >> zap(P[0,0,0,0,1,2,3,4,5,0,6,7,8,3,2,1].shuffle().mirror(), dur=1, sus=1, chop=P[2,1,0,2,4,4].shuffle().mirror(), tremolo=0.1, vib=0.1, dist=0.2, oct=(4, 5), amp=PEuclid(P[2,4,5,3,7].shuffle().mirror()*2, 8))
d1 >> play(P["<--([--]-)-><  o >"], amp=(PEuclid(P[4,5,6].shuffle().mirror(),8)*PWhite(1,1.5), 1), delay=PRand(list(drange(-0.02,0.02,0.0005))), pan=(PWhite(-0.8,0.8), 0), room=0.3, mix=0.3)
k1 >> play(P["X "], sample=2, amp=3)
s1 >> pluck(P[P[1,0,0,-1],0,P[0,0,0,-1],0,0,P[0,0,0,3],0,1], oct=(4,5), dur=0.25, amp=PEuclid(5,8)*1.6, dist=0.03)
b1 >> varsaw(s1.degree, oct=(3,4), dur=0.25, amp=PEuclid(P[5,4,3,6],8), sus=0.2, lpf=900, lpr=0.2, dist=(0,0.3))
b1 >> sawbass(s1.degree, sus=0.1, dur=0.25, amp=PEuclid(P[3,4,5,3,3,4].shuffle().mirror(), 8))

g = Group(k1,b1,s1,d1).solo(),
g = Group(b1,s1,d1).solo()
g = Group(s1,d1).solo()
g = Group(s1,d1).solo()
g.hpf=0;g.hpr=0.2;
