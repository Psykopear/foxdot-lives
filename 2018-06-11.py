from FoxDot import *
Clock.clear()
Scale.default=Scale.locrian
Root.default=var(P[0], 1)
m = Master()

def drange(start, end, step=0.1):
    r = start
    while r <= end:
        yield r
        r += step


s1 = Player()
s1 >> feel(var(P[0,0,0,1,5,2,3,4,].shuffle().mirror(), 1), chop=5.5, formant=sinvar([0,1],16), shape=sinvar([0.5,0],8))

d2 = Player()
d2 >> play("-", dur=0.25, sample=PRand(list(range(5))), amp=PWhite(0.8,1)*PEuclid(P[12,11,10,9,14,8].shuffle().mirror(),22)*2, delay=list(drange(-0.02,0.02,0.005)))

s2 >> sitar(s1.degree, dur=P[0.25], sus=1, oct=4, amp=0.9*PEuclid(6,11))
b1 >> evilbass(s1.degree, dur=0.25, amp=PEuclid(P[5,4,3],8)*1.8, sus=0.3)
k1 >> play("X ", sample=2, amp=4.5)

m.hpf=0;m.hpr=0.2;
Group(k1,b1,s2).amplify=var([1,0],[28,4])

Clock.bpm=144
