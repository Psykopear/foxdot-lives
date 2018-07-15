from FoxDot import *

Scale.default=Scale.phrygian

s1 >> ambi(s2.degree, chop=(4,3,2), formant=(0.1,0.2,0.3), amp=linvar([0,1.3],0.25))
s2 >> sitar(var([0,3,2,1],[10,2,2,2]), oct=(4,5), amp=0.5, dur=P[1,0.5,0.25,0.5,0.25,0.5])
d1 >> play("-", sample=PRand(list(range(5))), amp=PWhite(0.4,1), dur=PRand([0.5,0.5,0.5,0.25]), pan=PWhite(-0.8,0.8))

Group(s1,s2,d1,s3).solo()


Master().amplify=var([1,1],[.5,.25])
b1 >> sawbass(s2.degree, dur=PRand([0.5,0.25]), sus=0.3, amp=2).stop()
k1 >> play("<X h><  Ou>", hpf=PWhite(300,6000), hpr=0.3, dur=0.25, sample=2, amp=(0.7,0.5), room=(0.2, 0.4), mix=(0.2,0.3))
k2 >> play("x-", sample=5, amp=0.7).every(8, 'stutter', PRand([1,2,4])).stop()
d2 >> play("  h ", hpf=0, echo=0.2, amp=1.2, shape=(0,0.5), dur=0.5).stop()
b2 >> bass(P[2,0,0,0, 0,0,3,0, 0,0,0,0, -1,0,0,0], amp=P[1,1,1,1, 1,0,1,1, 1,0,1,1, 1,0,1,1]*1, dur=0.25, sus=0.2, oct=5)

Group(k1,k2,b2).stop()

Clock.bpm=180


s3 >> pluck(0, chop=4, oct=(4,5,6), shape=0.2, formant=0.1)


Master().hpf=var([500],[2]);Master().hpr=0.3;Master().mix=0.2;Master().room=0.2
Master().hpf=0;Master().hpr=0;Master().mix=0;Master().room=0


Scale.default=Scale.dorian

Root.default=var([0,7,5,3,1,1],[16,8,2,2,2,2])

s1.reset() >> arpy(b1.degree, shape=(0,0.2,0.3), dur=0.5, chop=0, amp=1.7)
d1 >> play("-")
b1 >> dab(dur=PRand([0.5,0.25]), sus=0.5, amp=0.4)
d2 >> play("o  -  =", echo=0.2, sample=PRand(list(range(5))), amp=0.1, shape=(0,0.6), formant=(0.4,0), dur=PRand([1,2,.5,0.25]), hpf=200)
b1 >> sawbass(hpf=200, var([0,7,5,3,1,1],[16,8,2,2,2,2]), dur=Fraction(1,3), amp=P[0.6,0.8,1]*2.0, sus=0.1)
k1 >> play(" --", dur=Fraction(1,3)).every(4, 'stutter', PRand([1,2,4]))
s2.reset() >> varsaw(b1.degree, amp=0.5,  oct=(4,5), dur=Fraction(1,3), sus=0.2, chop=0)


Master().hpf=var([2000],[2]);Master().hpr=0.2;Master().mix=0.4;Master().room=0.4
Master().hpf=0;Master().hpr=0;Master().mix=0;Master().room=0
Master().amplify=var([1,1],[.25,.125])


s1 >> klank(b1.degree, dur=0.25, chop=1, amp=expvar([-1,3],0.5), shape=(PWhite(0.2,0.4),PWhite(0.3, 0.8)))
d4 >> play("  O ", dur=0.5, amp=0.5, room=0.3, size=0.3)
k1 >> play("X-", sample=2, amp=1.4,  shape=(0,0.2)).every(4, 'stutter', PRand([1,2,4]))
b1.reset() >> bass(var([-6],[4]), dur=0.5, amp=P[0,1], shape=(0,0.2))

Group(s1,k1,b1).solo()
