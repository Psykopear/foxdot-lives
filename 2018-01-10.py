from FoxDot import *

Root.default=0

Scale.default=[0,1,4,5,7,8,11]
Scale.default=Scale.phrygian

s1 >> ambi(var([0,1,3,2,1,0,-2],[4,6,2,2,1,0.5,0.5]), oct=5, shape=(0,linvar([1,0],16)), formant=(0,linvar([0,1],16)), chop=3)
b1 >> sawbass(s1.degree, dur=Fraction(1,3), sus=0.2, rq=0.2, cutoff=800, amp=P[0.8,0.9,1]*2)
k1 >> play("(X o{[XX]o}O)( -)(-- )", dur=Fraction(1,3), sample=2, amp=0.9, hpf=400)
k2 >> play("X ", sample=1, amp=0.3, shape=1, dur=1, hpf=400, swell=400, hpr=0.2, formant=0.8, chop=0, echo=0.1)
k3 >> play("<x ><--O->", sample=5, amp=0.4, room=1, mix=1)
k4 >> play("<x ><--O->", sample=5, amp=(1,1))
