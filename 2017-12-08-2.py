from FoxDot import *

Scale.default=Scale.locrian

Clock.bpm=160


Root.default=var([0,0,2,0],[4,4,4,4])

s1 >> klank(0, dur=4, sus=4, hpf=100, hpr=0.2)
s2 >> arpy(0, dur=0.25, chop=0, stutter=2, echo=1.5,  hpf=(PWhite(100,2000),PWhite(100,2000)), hpr=0.2, formant=(PWhite(1,0),PWhite(0,2)), amp=PRand([0,1,1.8]), oct=(5,6))


d1 >> play("(- [--]-)", sample=PRand([0,1,2,3]))
d2 >> play("=       ", sample=2)
d3 >> play("  {o[oh]} ", sample=5)
drums = Group(d1,d2,d3)
drums.formant=PWhite(0,2)
drums.shape=PWhite(0,1)
drums.amplify=expvar([1,0],0.5)
k1 >> play("<X-X-X{[-x] }X[--]><  O >", dur=0.5, sample=2, amp=(1,0.7))

Group(k1,b1).mix=0; Group(k1,b1).room=0; Group(k1,b1).shape=0;

Group(s1,s2,d1,d2,d3).amplify=expvar([0,1],0.5)*expvar([0,2],0.5)
Master().mix=0.0;Master().room=0.3;Master().shape=0.0; Master().hpr=0.2; Master().hpf=0
Master().mix=0;Master().room=0;Master().shape=0



b1 >> sawbass(PRand([0,0,0,0,2,3]), dur=0.25, amp=P[0,1,1,1, 0,1,0,1, 1,0,1,0, 0,1,1,1]*3, sus=0.1, cutoff=900, rq=0.2, )
b1 >> sawbass(PRand([0,0,0,0,2,3]), dur=0.5, amp=P[0,1]*3, sus=0.1, cutoff=900, rq=0.2, lpf=0)

b1 >> bass(PRand([0,0,0,0,2,3]), dur=0.5, amp=P[0,1], sus=0.3, lpf=600, lpr=0.1)
