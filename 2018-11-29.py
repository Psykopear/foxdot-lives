FoxDot.start

from FoxDot import *

Clock.clear()

Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()


s1 >> klank(var([0,-1,2,1],8), chop=1, dur=0.25, sus=0.2, formant=(0,sinvar([0,1],16)))

d1 >> play("-", dur=0.25, sample=PRand(list(range(3))), pan=PWhite(-1,1), amp=P[1.0,0.8,0.9,0.8])

d2 >> play("h o ", room=0.6, mix=(0,1)).sometimes("amen")

b1 >> sawbass(s1.degree, dur=PDur(P[3,5,4],8), sus=0.2, lpf=PWhite(300,1900), lpr=0.2, hpf=0)

k1 >> play("X ", sample=2, mix=(0,0.8), room=0.3, amp=0.4).sometimes('stutter', 4, dur=3)

Group(k1, b1).solo()

Master().hpf=400;Master().hpr=0.2;Master().room=0.5;Master().mix=0.3
Master().hpf=0;Master().hpr=1;Master().room=0;Master().mix=0


s3.reset() >> sitar(s1.degree + PRand([0,0,0,0,0,1,2]), dur=PDur(P[7,11,13,12],16), amp=0.9, shape=(0,0.1), formant=sinvar([0,2],16))


(
    k1.reset() >> play("<X|-3|><  * >", sample=2, mix=(0,0.8), room=0.3, amp=0.0).sometimes('stutter', 4, dur=3),
    b1.reset() >> evilbass(var([0,-1,2,0],8), dur=0.25, amp=P[0,1,1,1, 1,0,1,1, 1,1,0,1, 1,1,1,0],),
    )




### INTRO
Scale.default=Scale.major
Root.default=var(P[0], 1)
Clock.bpm=105

s1.reset() >> star(var([5,6,7,6],[7.5,0.5]), oct=(5), formant=0.5, dur=P[7.5,0.5], amp=0.3, room=0.7, mix=0.4).spread()
s2.reset() >> pluck(P[6,7,9,7], oct=(5,3), dur=0.25, room=0.7, mix=0.5, shape=(0,PWhite(0.2,0.4)), hpf=PWhite(0,3000), hpr=0.1, amp=0.9).spread()
b1.reset() >> sawbass(var([3,4,5,4],[7.5,0.5]), dur=P[3/4,3/4,2/4], sus=0.3, lpf=1300, lpr=0.2, amp=1.0, shape=(0,0.1), room=0.3, mix=0.1)
s3.reset() >> ambi(4, oct=6, mix=0.9, sus=0.7, room=0.9, dur=2, echo=0, amp=0.5).spread()
s4.reset() >> ambi(2, oct=6, sus=0.7, mix=0.9, room=0.9, dur=P[0.5,1.5], echo=0, amp=0.5)
###################################

(
    b1.reset() >> sawbass(var([3,4,5,4],[7.5,0.5]), dur=P[3/4,3/4,2/4], sus=0.3, lpf=1400, lpr=0.3, amp=0.9, shape=(0,0.2), room=0.3, mix=0.2, hpf=0),
)
s1.reset() >> star(var([5,6,7,6],[7.5,0.5]), oct=(5), formant=sinvar([0,1],16), dur=P[7.5,0.5], amp=0.3, room=0.7, mix=0.4).spread()
s2.reset() >> pluck(P[6,7,9,7], oct=(5,3),dur=0.25, room=0.7, mix=0.2, shape=(0,PWhite(0.2,0.4)), hpf=PWhite(1000,3000), hpr=0.1, amp=0.7).stop()
s3.reset() >> ambi(4, oct=6, mix=0.9, sus=0.7, room=0.9, dur=2, echo=0, amp=0.5).spread().stop()
s4.reset() >> ambi(2, oct=6, sus=0.7, mix=0.9, room=0.9, dur=P[0.5,1.5], echo=0, amp=0.5).stop()




### REGGAE STRUCTS, non proprio
Clock.bpm=130
(
    k1.reset() >> play("  ", sample=2),
)
b1.reset() >> sawbass(var([1,3, 2,1, 3,4, 2,-1],[7.5,0.5]), dur=PDur(P[5,9,8,7],16), sus=0.3, amp=1.5, lpf=PWhite(400,2000), lpr=0.1)
s2.reset() >> ambi(b1.degree, chop=4, amp=1.0, formant=(0,sinvar([1,2],16)), shape=(0,sinvar([0.2,0],16))))
(
    d1.reset() >> play("s", dur=0.25, amp=P[1,0.5,0.8,0.5], room=0.3, mix=(0,0.8), pan=PWhite(-1,1)).spread(),
    k1 >> play("X ", sample=2, room=0.8, mix=(0,0.9), amp=1.0),
)

Group(b1).solo()
###########################

(
    s5.reset() >> sitar(b1.degree + PRand([0,0,0,0,0,1,2]), chop=0, dur=0.25, hpf=PWhite(0,3000), hpr=0.3, amp=0.3).degrade().stop()
)




### BLUES RIFF
Clock.bpm=120
Scale.default=Scale.mixolydian
Root.default=var(P[4], 1)
(
    b1.reset() >> sawbass(var([0,3],[7,1]), amp=1, dur=PDur(P[3,4,5,4],8), delay=0, sus=0.2),
    k1.reset() >> play("  ", sample=2, amp=1, room=0.8, mix=(0,0.9)),
    d2.reset() >> play("s", echo=0, dur=0.25, amp=P[1,0.5,0.8,0.5])
)
s4.reset() >> prophet(P[7,6,4,2], dur=8, oct=5, shape=(0.4), chop=(32), formant=(0,0.2), amp=1).stop()
##########################################


Clock.bpm=120
s2.reset() >> razz(b4.degree, dur=PDur(5,8), sus=0.3, amp=1.6).stop()
s3.reset() >> prophet(b4.degree, dur=PRand([1,0.5]), sus=0.4, shape=(0,0.3), formant=(0,0.3), amp=1.5).stop()
Group(k1,b4).solo()

(
    b4.reset() >> sawbass(var([0,1,0,-1],8), dur=1/4, sus=0.25, amp=P[0,1,1,1, 1,1,0,1, 1,0,1,1, 1,1,1,0]*3, lpf=PWhite(500,2000), lpr=0.1),
    k1.reset() >> play("V   ", dur=1/4, sample=2, room=0.6, mix=(0,0.8)),
    s1.reset() >> pluck(b4.degree + PRand([0,0,0,1,2,3]), dur=PDur(P[3,5,7,4],8), sus=0.4, amp=3.0, oct=(4,5), shape=(0,0.3), formant=(0,0.4)).stop(),
)

d1.reset() >> play("afkjsaldk", hpf=PWhite(100,3000), hpr=0.2, echo=(0,0.1), mix=(0,0.7), room=0.4, amp=1.0, dur=1/4)

Group(k1,d1,b4).solo()
Master().hpf=2000;Master().hpr=0.3;Master().room=0.5;Master().mix=0.4
Master().hpf=0;Master().hpr=1;Master().room=0;Master().mix=0

Scale.default=Scale.phrygian
Root.default=var(P[0],1)
m = Master()
#########






















# THE END
Clock.clear()
