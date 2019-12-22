from FoxDot import *

Clock.bpm=160

Scale.default=Scale.major

s1.reset() >> space(var(P[0,2,4,6,7,6,4,2],1), mix=0.5, room=(0,0.5), oct=(4,5), amp=0.8, chop=8)
b1.reset() >> bass(var(P[(9,13),(0,7),(2,9),(0,7),(1,8),(2,9)], 32), dur=PDur(P[4,3,5,3],8), lpf=PWhite(200,2000), lpr=0.3, sus=0.6, amp=0.5)
d1.reset() >> play("h--=", hpr=0.2, hpf=PWhite(100,3000), amp=0.5).sometimes("amen")
k1 >> play("X-", sample=2, amp=0.6)

Scale.default=Scale.phrygian

s1.reset() >> sitar(var(P[0,3,1,-1],8)+ PRand([1,0,0]), mix=0.5, room=(0,0.5), oct=(5), dur=PDur(3,8), pan=PWhite(-1,1), amp=0.7, chop=4).stop()




Scale.default=Scale.phrygian

m = Master()

m = Group(s1,d1,b1)

m.hpf=700;m.hpr=0.2;m.mix=0.3;m.room=0.3;

Scale.default=Scale.blues

d1.reset() >> play("hjOh", hpr=0.2, hpf=PWhite(100,3000), formant=PRand([0,1,2,3,4]), echo=(0,0.1), amp=0.5, room=0.5, mix=0.5).sometimes("amen").spread().stop()
k1.reset() >> play(" [  ]" , hpf=0, room=(0,0.3), hpr=0.3, sample=2, amp=0.6).sometimes("stutter", 3, dur=1)


b1.reset() >> evilbass(var(P[0],[6,2]), oct=(4), hpf=0, dur=PDur(8,8), delay=0.25, lpf=PWhite(2000,2000), lpr=0.2, sus=0.4, amp=P[0,0.4,0.8,1]*0.00)
s2.reset() >> pluck((s3.degree, s3.degree + 2), shape=P[0.1,0.2], formant=PRand([0,0.1,0.2,0.3,0.4,0.5,0.6]), dur=PDur(5,8), amp=0.0)


Scale.default=Scale.justMinor

s3.reset() >> klank(b3.degree, oct=5, pan=PWhite(-1,1), formant=sinvar([0,2],16), dur=PDur(4,6), chop=2)
s4.reset() >> orient(b3.degree + PRand([0,0,0,0,0]), dur=PDur(3,6), oct=4, amp=0.3, chop=2)
b3.reset() >> dbass(var(P[0,1,3,-2,-1,1], P[8,6,2), sus=0.4, amp=0.4, dur=PDur(4,6))
d1.reset() >> play(P[" --"], dur=1/3, amp=0.5)

m = Master()

m = Group(s1,d1,b1)

m.hpf=3404;m.hpr=0.4;m.mix=0.7;m.room=0.8;
