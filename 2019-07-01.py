from FoxDot import *

Scale.default=Scale.phrygian


Clock.clear()


SynthDefs

s1.reset() >> klank(b1.degree, oct=(3,5), chop=(14,28), amp=0.3, hpr=0.2, hpf=400, shape=0.2, formant=sinvar([0,1],14), dist=0.3, pan=sinvar([-1,1],14))
d1 >> play("*n- y*- hXhH- ", room=0.4, mix=0.4, echo=0.1, hpr=0.1, hpf=PWhite(100,2000)).sometimes("amen").spread()
k1 >> play("V VxV Vxx[xx]V Vx", sample=2, shape=(0,0.1), room=(0,0.3), mix=(0,0.3)).sometimes("amen")
b1 >> evilbass(var([0,2,-1],[14,7,7]), dur=PDur(P[3,4,2],7), amp=(0.7), sus=0.8, oct=(4))


SynthDefs

Scale.default=Scale.yu

s2 >> pluck(P[0].shuffle().offadd(2).stutter(2), chop=(2,4), oct=(4,5), dur=0.5)
d2 >> play("X-X- X( [  ])X", sample=2).sometimes("stutter", 3, dur=1)
b1 >> bass(s2.degree[0], dur=PDur(5,8), oct=(5), sus=0.2, amp=0.9)
d3 >> play(" -*- (*-)(-*)-").spread().sometimes("amen")


SynthDefs

Scale.default=Scale.prometheus

Scale.prometheus

Master().chop=2

s3.reset() >> quin((0,2,4), amp=0.5, dur=8, chop=32, formant=sinvar([0,1],16))
b3.reset() >> dbass(dur=PDur(5,8), delay=PRand([0.25,0.5,0]), amp=1)
k3.reset() >> play("(Sj)(jH)[jj](j=)").spread()
k4.reset() >> play("X -X- X -X -", amp=1, sample=2, room=(0,0.5), mix=(0,1))







s3 >> klank(var([0,3,-1],[8,4,4]), chop=4, formant=sinvar([0,1],16))
d3 >> play("*-h-").often("amen")
k3 >> play("X ", sample=2)
