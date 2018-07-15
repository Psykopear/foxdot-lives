from FoxDot import *

p1 >> pluck([0,[4,6,7]], dur=PDur(3,8), sus=1, coarse=PRand([0,2,4]), shape=0.3, formant=linvar([0,1],16), oct=4).spread() + var([0,(0,9)],[12,4])

s1 >> saw(cut=0.5, dur=0.25, sus=0.5, amp=PRand([1,0], seed=1)[:16], shape=0.5, vib=12) + var([0,P+(2,4,[6,7])],[3,1])

s2 >> sitar([var([0,-1,-4],16),[7,P*(7,6,4)]], dur=2, pan=1)
s3 >> sitar([4,2,[1,P*(1,2)]], oct=6, pan=-1, dur=var([1,[1/2,1/4]],[12,4])) + var([0,2],[12,4])

d1 >> play("<(x )( x){h[hx]}(s(x[xx]))><{-[--]}><  i >", sample=(2,-1,0), amp=(1,1,1))

b1 >> bass(var([0,-1,3],16), dur=16, sus=4, shape=1, room=1, mix=1, chop=0, echo=0).spread() + (0,PRand([6,7,9]))

b1.solo()
