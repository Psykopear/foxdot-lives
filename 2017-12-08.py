from FoxDot import *

Clock.bpm=150

Scale.default=Scale.phrygian

s1 >> klank(P[0,0,0,-1,3,2], dur=P[4,4,4,2,1,1], oct=(4,5), sus=4)
s2 >> arpy(s1.degree, dur=Fraction(1,3), formant=PWhite(0,2), hpf=PWhite(400,2000), hpr=0.3, sus=0.7, amp=P[0,1,1,0, 0,1,1,1, 1,0.7,0.8,1, 1,0,1,0])
s3 >> pluck(s2.degree, dur=1, chop=3, shape=(PWhite(0,1),PWhite(0,1)), hpf=(PWhite(100,1000),PWhite(200,2001)), hpr=PWhite(0.2,0.5))

b1 >> sawbass(s1.degree, dur=Fraction(1,3), sus=0.2, formant=(0), chop=0, hpf=0, hpr=0.3, cutoff=900, rq=0.1, amp=P[0.3,1,1]*3)
b1.stop()

d1 >> play("(- [ --]-)", sample=PRand([1,0,2]), dur=1)
d2 >> play("(X  )(  [Xo])( o )(=[ --])", sample=2, hpr=0.2, shape=0.3, mix=0.2, room=0.2, hpf=(PWhite(100,3000),PWhite(100,3000)))
d3 >> play("x x x( x [ x] )", sample=5, amp=1, hpf=0, dur=0.5)
d4 >> play("[ --]", dur=1, sample=2, amp=1)
Group(s1,s2,s3,d2).amplify=expvar([0,4],0.5)
Group(s1,s2,s3,d2).stop()
Group(d1,d2).formant=PWhite(0,3)

Group(d4,s3,b1).solo()

Master().hpf=900; Master().mix=0.2; Master().room=0.2

Clock.clear()


s4 >> sitar((P[0],P[0,0,0,-1,3]), chop=4, dur=P[4,4,4,2,2]/2, echo=0.25, formant=(PWhite(0,1),PWhite(0,1)), shape=0.4)
k1 >> play("X-X-X(-X-[-X]-)", sample=2, amp=1, hpf=0, dur=0.5)
b1 >> sawbass(P[0, PRand([0,1,2,4])], dur=0.25, amp=P[0,1,1,1, 0,1,0,1, 0.5,0,1,1, 1,0,1,1]*3, sus=0.2, cutoff=400, rq=0.2)
d1 >> play("[--]-[-]--", formant=(PWhite(0,2), PWhite(0,1)), pan=PWhite(-1,1), dur=0.25, hpf=(PWhite(0,2000),PWhite(200,1000)), hpr=0.2)

Group(s4,k1).solo()

Master().amplify=0
