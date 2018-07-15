from FoxDot import *

Clock.bpm=140

Root.default=var([0,2,5,3,2],[8,8,8,4,4])

s1 >> klank()


# I added a new synth
# I need to fix some default paramters
b1 >> sawbass(P[0,PRand([0,1,2,3,4,5]),0], scale=Scale.phrygian, oct=(3), amp=PRand([0,1,1,0.7])*0.20, hpf=0, sus=0.01, dur=0.25, cutoff=900, rq=0.2)

s2 >> varsaw(0, scale=Scale.phrygian, oct=(5,6), dur=0.25, chop=4, amp=0.4, bpf=linvar([400, 4000]), bpr=1, pan=(PWhite(-1,0),PWhite(0,1)), shape=(0.8,0.7))
k1 >> play("V-", room=1, mix=0.3)

d1 >> play("<(o n)><(n  )(-- [--])>", hpf=linvar([100,2000],16), hpr=0.1, formant=linvar([0,1],8), shape=0.1, room=0.7, mix=0.2)


Master().hpf=10000
Master().room=1
Master().mix=0.9


