from FoxDot import *

m1 >> arpy()
m1.oct=(5,6)
m1.degree=P[0,0,0,0,0, 2,2,3,3,3, 2,2,3,3,3, -2,-2,0,0,0]
m1.root=(0,5)
m1.scale=Scale.chromatic
m1.dur=P[1,0.75,0.75,1,0.5]
m1.sus=0.6
m1.delay=0
m1.room=0.5
m1.mix=0.2

m2 >> klank(m1.degree, sus=0.3, dur=1, scale=Scale.chromatic, chop=2, hpr=0.2, hpf=linvar([100,2000],16))


d1 >> play()
d1.degree="<-   - - -  -><{- }{- [--]}>"
d1.sample=(0,PRand([4,2,3,0]))

d2 >> play()
d2.degree="  "
d2.sample=1

d3 >> play()
d3.degree="o    o  "
d3.sample=8
d3.amp=0.3
d3.room=0.4
d3.mix=0.3


Group(d1,d2,d3).amplify=var([1,0],[28,4])


b1 >> sawbass(m1.degree, oct=3, sus=0.001, rq=0.2, cutoff=300, scale=Scale.chromatic, dur=0.25, amp=P[0,0,1,0, 0,0,1,0, 0,1,0,1, 0,0,1,1]*1.5, shape=0.0, formant=(0.1,0.0))
b2 >> saw(b1.degree, oct=3, scale=b1.scale, dur=b1.dur, sus=0.3, amp=b1.amp, lpf=400)

b2.degree=22



Master().room=0.3
Master().mix=0.2
Master().hpf=expvar([0,2000],64)
Master().hpr=0.2

Master().room=0.0
Master().mix=0.0
Master().hpf=0
Master().hpr=1

Root.default=var([-2,0,-2,1,0],[8,8,8,4,4])
Root.default=0

f1 >> arpy(P[0,(0,12,16),(0,12,16),0,(0,12,15), 0,(0,12,15),(0,12,15),0,(0,12,16)], dur=P[.5,.5,.5,.25,.25], sus=0.5, room=1, mix=0.3, scale=Scale.chromatic, chop=0)

Group(b1,d1).amplify=var([1,0],[28,4])
Master().amplify=var([1,0,0],[28,4,400])

b1 >> pluck(m1.degree,dur=PRand([0.5,0.25]), sus=0.2, amp=P[0,1,1,0, 0,1,0,1, 0,1,1,0.5, 0,1,0,1]*1.4)
d1 >> play("<V ><  o  >< {-[--]}>", sample=0, hpf=0).stop()

print(SynthDefs)



s1 >> pluc((0), dur=P[0.5, 0.25, 0.25], oct=4, sus=0.2, formant=(0.5,0.3), pan=(PWhite(1,0), PWhite(1,0)), amp=P[0,1,1,0, 0,1,0,1, 0,1,1,0.5, 0,1,0,1]*1.4)
s1 >> arpy(PRand([0,5]), oct=4, scale=Scale.chromatic, sus=2, dur=0.25, amp=P[0,0,1,0, 0,0,1,0, 0,1,0,1, 0,0,1,1]*1.5, formant=(0,0.3,1), shape=0.2)
p1 >> play("n[nn]", shape=(0,1), sample=3, chop=4)
k1 >> play("={ -}O{[ooo] [---]}", dur=1, sample=1, hpf=linvar([100,2000],16), hpr=0.1, amp=2, room=0.5, mix=0.2)
k2 >> play("V ", amp=1.5).solo()


s1.solo()
