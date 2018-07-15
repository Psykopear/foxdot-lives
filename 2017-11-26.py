from FoxDot import *

Clock.bpm=160
Root.default=var(P[0,2,5,3,2]+7,[8,8,8,4,4])
Root.default=0



s1 >> sitar(0, oct=4, dur=0.25, chop=.5, hpf=linvar([1000,4000],16), sus=0.2, formant=linvar([0,3],8), hpr=0.2, amp=1.0, shape=0.3, room=1, mix=0.2, echo=16, slide=0, delay=0)
k1 >> play("<X><[ ]><(  o )>", sample=(2,2,2), amp=(1,1,1), dur=1, room=0.8, mix=0.2, hpf=0, hpr=0.2).every(16, 'stutter', 2)





b1 >> sawbass(PRand([0]), hpf=linvar([0, 0]), hpr=0.5,  scale=Scale.phrygian, amp=P[0,1,1,1], sus=0.02, oct=(3), dur=PRand([0.25]), cutoff=900, rq=0.1, drive=2)
b1.stop()


s1 >> saw(0, oct=(4), dur=2, sus=2, shape=0.2, pan=-0.5, formant=0.2)
s2 >> saw(s1.degree + 0.2, oct=(4), dur=2, sus=2, shape=0.1, pan=0.5, formant=0.3)

Group(s1,s2).chop=4
Group(s1,s2).amp=PRand([1.0])
Group(s1,s2).room=1
Group(s1,s2).mix=0.5
Group(s1,s2).shape=(0.2, 0.8)
Group(s1,s2).hpf=linvar([2000, 1000], 16)

Group(d1,d2,d3).stop()
d1 >> play("(o )( oi)", sample=(2,4), pan=(PWhite(-0.8,0),PWhite(0,0.8)), formant=(PWhite(0,0.8),PWhite(0.8,0)))
d2 >> play("<(=-    n )><(-  n(n o i))>", chop=4, shape=0.4).every(4, 'stutter',2)
d3 >> play("( n{[oo]o} )", amp=1.5, room=0.2, mix=0.2).stop()
d4 >> play("[=---]", dur=1, shape=linvar([0.8,0.3]), hpf=linvar([400,2000],8), hpr=0.1, mix=0.3, room=0.7, formant=linvar([0,1],8), chop=3, amp=2).every(4, 'stutter', 3)
d4.stop()

# , shape=0.8, hpf=linvar([400,2000],16), hpr=0.1, mix=0.1, room=0.7, dur=1, formant=linvar([0,1],8), chop=3, amp=2).every(4, 'stutter',3)

p1 >> arpy(P[0,(0,12,16),(0,12,16),0,(12,15), 0,(0,12,15),(0,12,15),0,(12,16)], scale=Scale.chromatic, oct=(5), dur=P[.5,.5,.5,.25,.25]*1, amp=P[1,1,1,1,1, 0,1,1,1,1]*2, sus=0.5, formant=(0.1,0.2))

p1.hpf=0


p1.stop()

Group(d4,p1,s1).solo()
Master().play()

p1.stop()


Master().hpf=0
