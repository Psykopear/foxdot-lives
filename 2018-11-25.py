FoxDot.start
from FoxDot import *

Clock.clear()

Scale.default=Scale.lydian

Scale.default=Scale.phrygian
Scale.default=Scale.aeolian
Scale.default=Scale.mixolydian
Root.default=var(P[4], 1)
m = Master()
Clock.bpm=100




### INTRO
Scale.default=Scale.major
Root.default=var(P[0], 1)
Clock.bpm=100
Clock.clear()
s1.reset() >> star(var([5,6,7,6],[7.5,0.5]), oct=(5), formant=0.5, dur=P[7.5,0.5], amp=0.1, room=0.7, mix=0.5).spread()
s2.reset() >> pluck(P[6,7,9,7], oct=(5,3),dur=0.25, room=0.8, mix=0.6, shape=(0,sinvar([0.2,0.4],16)), hpf=sinvar([0,3000],16), hpr=0.2, amp=0.2).spread()
b1.reset() >> sawbass(var([3,4,5,4],[7.5,0.5]), dur=P[3/4,3/4,2/4], sus=0.4, lpf=2900, lpr=0.2, amp=0.8, shape=(0,0.1), room=0, mix=0)
s3.reset() >> ambi(4, oct=6, mix=0.9, sus=0.7, room=0.9, dur=2, echo=0, amp=1).spread()
s4.reset() >> ambi(2, oct=6, sus=0.7, mix=0.9, room=0.9, dur=P[0.5,1.5], echo=0, amp=1)

Group(s3,s4).amplify=sinvar([0.8,1.2],16)


### REGGAE STRUCTS
Clock.bpm=130
d2 >> play("s", dur=0.25, amp=P[1,0.5,0.8,0.5], room=0.3, mix=(0,0.8))
b1.reset() >> sawbass(var([1,1, 2,2, 3,4, 2,-1],[7.5,0.5]), dur=PDur(P[9,6,7,5],16), sus=0.2, amp=0.9, lpf=900, lpr=0.2).stop()
k1 >> play("    ", room=0.8, mix=(0,0.9))

s2.reset() >> ambi(b1.degree, chop=4, amp=0.0)

### BLUES RIFF
Clock.bpm=120
Scale.default=Scale.mixolydian
Root.default=var(P[4], 1)
d1 >> play("  ", sample=2, amp=1)
b1.reset() >> sawbass(var([0,0],16), amp=P[0,1], dur=0.5, delay=0, sus=0.2)
s4 >> prophet(P[7,6,4,2], dur=8, oct=5, shape=(0.4), chop=(4,32), formant=(0,0.2)).stop()
d2 >> play(" ", dur=0.25, amp=P[1,0.5,0.8,0.5])

Group(b1,d1).solo()
k1 >> play("r ", sample=3)
k2 >> play("  ", sample=2)
b1 >> sawbass(0)
b1.amplify=var([1,0],[28,4])


#################################


# s4 >> sitar(var([0,3],16), oct=(4,5), hpf=(PWhite(400, 1000),0), hpr=0.2, dur=PDur(5,8)*2, amp=0.4).spread()
# d1 >> play("= |-1| -  ( [--])", amp=2).stop()
# p1 >> prophet(var([0,3], 16), dur=4, sus=4, oct=(4,5), amp=1, chop=PRand([4,8,16]))
# print(SynthDefs)
# g1.reset() >> arpy(var([0,3],16), dur=PDur(3,8), echo=(0), mix=0.3, room=0.3, formant=(0,4)).strum(0.03)
# k1.reset() >> 

# Master().room=0.6;Master().mix=0.4;Master().hpf=200;Master().hpr=0.3
# Master().room=0;Master().mix=0
# k1 >> play("X ")


# s1 >> ambi((0,P[2,2,4,4]), sus=1, dur=PDur(3,8), chop=4)
# s2 >> pluck(var([0,1],16), oct=(4,5), formant=(0,sinvar([0,1],16)), dur=PDur(3,8), sus=0.3).spread().sometimes('amen')
# s3 >> klank(s2.degree, dur=2, chop=8, sus=2, shape=(0,sinvar([0,0.4],8)))
# b1 >> sawbass(s2.degree, dur=PDur(P[5,3,7],8), sus=0.2)
# d1 >> play("=-", dur=0.25, sample=PRand(list(range(4))), amp=PWhite(0.8,1.2), pan=PWhite(-1,1)).degrade().stop()



# b1.reset() >> evilbass(var([3,4,5,4],[7,1]), dur=P[3/4,3/4,2/4], delay=0, amp=3, sus=0.4)
# k1.reset() >> play("X ", sample=2, hpf=0, hpr=0, amp=2)
# s1.reset() >> prophet(var([5,6,7,6],[7,1]), amp=0.8, dur=P[7,1])
# s2.reset() >> pluck(P[6,7,9,7], oct=(4,3,5),dur=0.25, room=0.3, mix=0.3, shape=(0,sinvar([0.2,0.4],16)), hpf=sinvar([0,3000],16), hpr=0.2)
# s3.reset() >> sitar(var([9,11],16), dur=8, sus=8, amp=1, oct=5, room=0.4, mix=0.4, chop=32, pan=PWhite(-1,1))
# n1 >> noise(hpf=1000, hpr=0.2, dur=16, sus=16, mix=0.8, room=0.8).stop()

# 4,6,4
