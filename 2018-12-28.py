FoxDot.start
from FoxDot import *
Clock.clear()
SynthDefs
m = Master()
m.amplify=0.8
# 0 DO
# 2 RE
# 4 MI
# 5 FA
# 7 SOL
# 9 LA
# 10 SI
# 12 DO
s1 >> klank(var([0,2,1,-1],8))
s2 >> ambi(s1.degree)
s3 >> prophet(s1.degree, dur=2, chop=8, amp=1)
s4 >> razz(s1.degree, dur=0.5, room=0.5, mix=0.5, shape=0.3, dist=0.2, amp=0.9)
s5 >> pluck(s1.degree, dur=PDur(3,8)).spread()
b1 >> sawbass(s2.degree, dur=4, sus=4, amp=1)
k1 >> play("[ssss]", sample=0, room=0.3, mix=(0,0.5), amp=1)
k1.reset() >> play("X X ", sample=2, amp=1.0, room=0.4, mix=0.3)

Scale.default=Scale.phrygian
Root.default=var(P[0], 1)


Master().hpf=500;Master().hpr=0.4;Master().formant=0.4
Master().hpf=0;Master().hpr=1;Master().formant=0

## INTRO
Scale.default=Scale.chromatic
Root.default=var(P[0,-3,4-12,4-12], 4)
Clock.bpm=65
Group(s2,s3).solo()

d1.reset() >> play("(x )(x )(s[ss])(x )", amp=1, formant=(0)).solo()
s5.reset() >> sawbass(dur=PDur(P[3,5,4,8],8), sus=0.2, amp=1.0, hpr=0.4, hpf=0, oct=(5)).stop()
s2.reset() >> klank((0,7), dur=2, sus=2, chop=P[4,8,16], amp=1.0, oct=(4,5))
s3.reset() >> razz((0,7), hpr=1, chop=P[16,4,8], hpf=PWhite(100,2000), dur=2, sus=2, amp=1.0, oct=(6), mix=0.3, shape=PWhite(0,0.3))

# s2.reset() >> klank((0,7), chop=P[4,16,8], dur=2, sus=2, amp=1, oct=(4,5))
# s3.reset() >> razz((0,7), hpr=1, chop=P[16,8,4], hpf=0, dur=2, sus=2, amp=1.0, oct=(5,6), mix=0.4, shape=PWhite(0.1,0.3))

# Basso
s5.reset() >> sawbass(dur=P[0.75], sus=0.2, amp=1.0, oct=(5))
s6.reset() >> pasha(dur=PDur(P[5,3,8,4],8), amp=1.0, sus=0.3, formant=PWhite(0,0.6), room=0.3, mix=0.5).spread().stop()

# SINEBASS
b1.reset() >> sawbass(dur=4, sus=4, amp=1.0, lpf=120)

Master().hpf=500;Master().hpr=0.4;Master().formant=0.4
Master().hpf=0;Master().hpr=1;Master().formant=0

####
s5.reset() >> sawbass(dur=PDur(P[3,5,4,8],8), sus=0.2, amp=0.2)
s6.reset() >> pasha(dur=0.25, amp=0.3, room=0.3, mix=0.3).degrade().spread()


Scale.default=Scale.chromatic
Root.default=var(P[7,5,4,2,0,0], 2.5)
Root.default=0
Clock.bpm=60
d1.reset() >> play("<[(t[tt])  ]><[ tt]>", amp=(0.6,0.3), pan=(PWhite(-0.8,0.8), PWhite(1,-1)), room=0.1, mix=(0,0.5), echo=P[0,0,0,0.00])
k1.reset() >> play("X(h )X( h) ", sample=2, amp=0.4, room=0.4, mix=(0,0.3))
d4.reset() >> play(" - - ", sample=2, amp=0.4, room=0.4, mix=(0.5))
d2 >> pluck(0, amp=0.6, sus=0.2, shape=0.0, dur=PDur(7,16)/2, oct=(5), pan=PWhite(-0.5,0.5), formant=0)
####


Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
Clock.bpm=120
d1 >> play("s", dur=0.25, amp=PEuclid(P[9,12,13,11],16)*PWhite(0.5,1.2), pan=PWhite(-1,1), room=0.4)
k1.reset() >> play(" [ (X )] ( X [XX])", sample=2, room=0.4, mix=(0,0.5), amp=1)
b1.reset() >> sawbass(P[1,0,0,P[0,0,0,7], 0,0,P[0,0,0,7],0, 0,0,0,0, P[0,0,0,5],0,P[0,0,0,2],0], dur=var([0.125,0.25], 16), amp=P[1,0,0,1, 0,0,1,0, 1,0,0,0, 1,0,1,0]*1.0, hpr=0.2, sus=0.2, oct=(6), hpf=0)
k2 >> play("X ", sample=2, room=0.3, mix=(0,0.5), amp=1)
b1.reset() >> sawbass(0, dur=var([0.25,0.125], 16), amp=P[1,0,0,0, 0,1,0,0, 0,0,1,0, 0,1,0,0]*1.0, hpr=0.6, sus=0.2, oct=(5), hpf=0)


Clock.bpm=160
Root.default=var(P[4], 1)
Scale.default=Scale.dorian

b1.reset() >> dbass(var([0,0,0,0],8), dur=PDur(3,8), amp=0.5, sus=0.4)
s2.reset() >> prophet(b1.degree, dur=1, amp=1.2, sus=0.2, shape=PWhite(0,0.2), formant=PWhite(0,0.4))
s3.reset() >> razz(b1.degree, sus=0.5, amp=1.2, formant=0, shape=1, chop=var([2,1],4), dur=PRand([1,0.5]))
s1.reset() >> snick(b1.degree, oct=(6), dur=1, formant=PWhite(0,1)).stop()

b1.reset() >> dbass(var([2,1,0,0],8), dur=PDur(3,8), amp=0.5, sus=0.4)
b1.reset() >> dbass(var([2,1,0,0],8), dur=PDur(3,8), amp=0.5, sus=0.5, chop=16, hpf=500, hpr=0.3, oct=6)

