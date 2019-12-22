from FoxDot import *

Scale.default=Scale.phrygian


s1 >> klank(var([0,0,2,-1],8), oct=(4,5), chop=(0,4), formant=sinvar([0,1],16)).stop()
d1 >> play("{[--]-}{-[--]}*{[--]-}", delay=P[0,0.01,0.02,0.01,-0.01,-0.02], dur=0.5, room=0.5, mix=0.5).stop()
b1 >> evilbass(s1.degree, dur=PDur(P[1,],8), delay=0.25, sus=1.8, oct=(4,5), shape=(0,0.1), room=(0,0.4), mix=(0,0.3), amp=0.6).stop()
k1 >> play("  ", sample=2, hpr=0.2, hpf=0, shape=(0,0.1,0.9)).sometimes("stutter", 2)
d2 >> play("h---", echo=(0,0.1), mix=(0,0.9), room=0.5).often("amen").stop()
s2 >> sitar(s1.degree + PRand([0,0,0,0,0,1,2]), amp=0.4, dur=PDur(P[3,4,5],8), sus=0.4).stop()


m= Master()

m.hpf=0;m.hpr=0.3;m.mix=0.5;m.room=0.2

Scale.default=Scale.locrian

b1.reset() >> sawbass(var([0,0,0,-1], 8), cutoff=PWhite(200,4000), dur=PDur(P[7],8), sus=0.1, shape=(0,0.1), room=(0,0.4), mix=(0,0.3), amp=expvar([0,1],0.5)).stop()
d1.reset() >> play("t-*-", amp=0.7, mix=0.3, room=0.5).often("amen").stop()

d1.reset() >> play(" ", sample=PRand(list(range(5))), dur=0.125, echo=(0), formant=0.5, shape=0.0, amp=1, hpr=0.2, hpf=sinvar([200,2000],16), pan=sinvar([-1,1],8)).stop()
s1.reset() >> prophet(0, dur=0.5, oct=(4,5,6), shape=0.3, room=0.5, mix=(0,0.5), chop=2, formant=PWhite(1,2), amp=0.5).stop()

Clock.bpm=60

k1.reset() >> play("  ", dur=0.5, sample=2, amp=1.2, hpr=0.2, hpf=0).sometimes("stutter", 2).often("stutter", 2, dur=2, hpr=0.2, hpf=600, echo=0.1, mix=0.4, room=0.4)
s2 >> pluck(var(P[0,0,0,-1,1],P[8,8,8,4,4]), dur=0.25, chop=2, pan=PWhite(-1,1), sus=0.3, formant=(0,0,0.2,0.2), oct=(4), amp=1.9)
b1.reset() >> evilbass(s2.degree, dur=PDur(P[3],8), formant=(0,0.8), mix=0.3, room=0.2, amp=(1), oct=(4), sus=0.8, )


Clock.clear()

m = Master()

m.hpr=0.3;m.hpf=(0);m.mix=0;m.room=0.8;
