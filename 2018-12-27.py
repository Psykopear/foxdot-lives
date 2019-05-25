FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.chromatic
Scale.mixolydian

Root.default=var(P[0,-3,4-12,4-12], 4)
Clock.bpm=65

m = Master()

SynthDefs

## INTRO
Scale.default=Scale.chromatic
Root.default=var(P[0,-3,4-12,4-12], 4)
Clock.bpm=65
s2.reset() >> klank((0,7), dur=4, sus=2, amp=0.5, oct=(4,5))
s3.reset() >> pads((0,7), hpr=1, hpf=0, dur=4, sus=4, amp=0.2, oct=(5,6), shape=PWhite(0,0.3))
####
s5.reset() >> sawbass(dur=PDur(P[3,5,4,8],8), sus=0.2, amp=0.2)
s6.reset() >> pasha(dur=0.25, amp=0.3, room=0.3, mix=0.3).degrade().spread()

########## EXECUTION
s2.reset() >> klank((0,7), dur=4, sus=2, amp=0.5, oct=(4,5)).stop()
s3.reset() >> pads((0,7), hpr=1, hpf=0, dur=4, sus=4, amp=0.1, oct=(5,6), shape=PWhite(0,0.2))
s4.reset() >> pluck(PRand([0,0,0,0,0]), dur=PDur(P[3,4,5,4],8)/2, sus=0.2, amp=0.6, dist=0.3)

(
    s2.reset() >> klank((7), dur=1, sus=0.2, amp=0.4, oct=(4,5)),
    s3.reset() >> pads((0,7), hpr=1, hpf=0, dur=1, sus=0.4, amp=0.2, oct=(5,6), shape=PWhite(0,0.0)),
)
s5.reset() >> sawbass(dur=PDur(P[3,5,4,8],8), sus=0.2, amp=0.7, oct=5).stop()
s6.reset() >> pasha(P[0,12], dur=PDur(P[5,3,8,4],8), sus=0.3, amp=0.3, room=0.3, mix=0.3, oct=5)



####### PARTE DUE
Scale.default=Scale.chromatic
Root.default=var([0], 4)
Clock.bpm=60
d1.reset() >> play("<[(t )  ]><[ tt]>", amp=(0.5,0.3), pan=(-1,1), room=0.1, mix=0.5).spread()
k1 >> play("X- X-", sample=2, amp=0.4, room=0.4, mix=0.3)
d2.reset() >> razz((0,0), amp=0.7, chop=0, sus=(0.2,0.1), dur=1/3, oct=(4,5))

###################
d1.reset() >> play("<[t  ]><[ tt]>", amp=(0.5,0.3), pan=(-1,1), room=0.1, mix=0.5).spread().stop()
k1 >> play("     ", sample=2, amp=0.8, room=0.4, mix=0.3)

Clock.bpm=90
d2.reset() >> razz((0,7), amp=0.4, chop=0, sus=(0.1,0.1), dur=1, oct=(5,6))

##### BOH
    Clock.bpm=60
    d1.reset() >> play("<[(t )  ]><[ tt]>", amp=(0.3,0.1), pan=(-1,1), echo=0, room=0.1, mix=0.5).spread()

    Clock.bpm=80
    d1.reset() >> play("<[(t ) ]><[ t]>", amp=(0.9,0.5), pan=(-1,1), echo=0, room=0.1, mix=0.5).spread()

    a1 >> audioin(rate=2, shape=0.0, formant=1, dist=0.3, amp=0.5).stop()
