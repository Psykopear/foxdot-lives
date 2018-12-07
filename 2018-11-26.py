FoxDot.start
from FoxDot import *
Clock.clear()

### INTRO
Scale.default=Scale.major
Root.default=var(P[0], 1)
Clock.bpm=100
s1.reset() >> star(var([5,6,7,6],[7.5,0.5]), oct=(5), formant=0.5, dur=P[7.5,0.5], amp=0.1, room=0.7, mix=0.9).spread()
s2.reset() >> pluck(P[6,7,9,7], oct=(5,3),dur=0.25, room=0.7, mix=0.5, shape=(0,PWhite(0.2,0.4)), hpf=PWhite(0,3000), hpr=0.1, amp=0.2).spread().degrade()
b1.reset() >> sawbass(var([3,4,5,4],[7.5,0.5]), dur=P[3/4,3/4,2/4], sus=0.3, lpf=1300, lpr=0.2, amp=0.8, shape=(0,0.1), room=0.3, mix=0.1)
s3.reset() >> ambi(4, oct=6, mix=0.9, sus=0.7, room=0.9, dur=2, echo=0, amp=0.5).spread()
s4.reset() >> ambi(2, oct=6, sus=0.7, mix=0.9, room=0.9, dur=P[0.5,1.5], echo=0, amp=0.5)
###################################

s1.reset() >> star(var([5,6,7,6],[7.5,0.5]), oct=(4,5), formant=0.5, dur=P[7.5,0.5], amp=0.3, room=0.7, mix=0.4).spread()
s2.reset() >> pluck(P[6,7,9,7], oct=(5,3),dur=0.25, room=0.7, mix=0.2, shape=(0,PWhite(0.2,0.4)), hpf=PWhite(1000,3000), hpr=0.1, amp=0.3).stop()

b1.reset() >> sawbass(var([3,4,5,4],[7.5,0.5]), dur=P[3/4,3/4,2/4], sus=0.3, lpf=1300, lpr=0.2, amp=0.8, shape=(0,0.1), room=0.3, mix=0.1)
s3.reset() >> ambi(4, oct=6, mix=0.9, sus=0.7, room=0.9, dur=2, echo=0, amp=0.5).spread().stop()
s4.reset() >> ambi(2, oct=6, sus=0.7, mix=0.9, room=0.9, dur=P[0.5,1.5], echo=0, amp=0.5).stop()




### REGGAE STRUCTS
Clock.bpm=130
(
    b1.reset() >> sawbass(var([1,3, 2,1, 3,4, 2,-1],[7.5,0.5]), dur=PDur(P[5,7],16), sus=0.3, amp=0.9, lpf=PWhite(700,2000), lpr=0.1).stop(),
    d1.reset() >> play("s", dur=0.25, amp=P[1,0.5,0.8,0.5], room=0.3, mix=(0,0.8), pan=PWhite(-1,1)).spread(),
    s2.reset() >> ambi(b1.degree, chop=4, amp=0.9),
    k1 >> play("  ", sample=2, room=0.8, mix=(0,0.9), amp=0.0),
)
###########################

(
    s5.reset() >> sitar(b1.degree + PRand([0,0,0,0,0,1,2]), chop=0, dur=0.25, hpf=PWhite(0,3000), hpr=0.3, amp=0.0).degrade()
)




### BLUES RIFF
Clock.bpm=120
Scale.default=Scale.mixolydian
Root.default=var(P[4], 1)
(
    k1.reset() >> play("X ", sample=2, room=0.8, mix=(0,0.9)),
    b1.reset() >> sawbass(var([0,-1,0,1],[7,1]), amp=1, dur=PDur(P[3,4,5,4],8), delay=0, sus=0.2),
    d2.reset() >> play("s", dur=0.25, amp=P[1,0.5,0.8,0.5])
)
s4.reset() >> prophet(P[7,6,4,2], dur=8, oct=5, shape=(0.4), chop=(4,32), formant=(0,0.2), amp=0.1).stop()
##########################################


### OUT, let's what happens
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()
#########
