from FoxDot import *

Clock.bpm=180

s1 >> klank()

Scale.default=Scale.locrian

a1 >> loop("/home/docler/Music/Samples/bitwig/Bitwig Drum Machines/Artificial Percussion/Percussion Sly A.wav")
a1 >> loop("*Snare*", sample=11, dur=PRand([0.25, 0.5, 0.25, 0.5]), amp=PWhite(0.5,1.5), delay=PRand([0, 0.01, -0.01]))
Samples.addPath('/home/docler/Music/Samples/bitwig')

t1 >> play('< _o{u }h n ><- --l- ->', sample=(5,2), hpf=0)
k1 >> play("V ", sample=2, amp=1.2)

b2 >> dab(b1.degree, sus=0.15, dur=0.25, amp=P[0,1,1,1, 0,1,0,1, 0.5,1,1,0, 0,1,1,0])

b1.reset() >> sitar(var([0,1,0,3,2,1],[4,4,4,2,1,1]), oct=(5,6.01), dur=PRand([0.5,0.25]), sus=0.1, amp=0.9)

print(SynthDefs)


Master().hpf=0;Master().hpr=0.2;Master().mix=0;Master().room=0;Master().formant=0

# I love distortion
d1 >> play("[--]l", sample=PRand([0,1,2,2]), hpf=(PWhite(0,1000), PWhite(0,1000)), hpr=0.2, amp=PWhite(0.5,1))
d2 >> play("  O ", sample=3,amp=1)
k1.reset() >> play("X[--]", shape=0.0, formant=PWhite(0,0), sample=2, amp=2)

b1.reset() >> sitar(var([0,3,0,4,3,2],[4,4,4,2,1,1]), oct=(5,6), shape=0.5, chop=1, dur=PRand([0.5,0.25]), sus=0.3, amp=linvar([0,1],0.5))

Group(b1, d1, d2, d3, d4).solo()


s1 >> prophet(oct=5, phase=0.9, cutoff=linvar([100,2000],16))
s2 >> nylon((0, PRand([(2,4),(3,5)]), 6), dur=0.5, sus=0.2, room=0.2, mix=0.2, oct=6, amp=PRand([0,0.7,0.8,1]), shape=(0.7,0.9))
s3 >> scratch(oct=5, amp=3)

d1 >> play("(- [--]-)", sample=PRand([0,1,2,3]), amp=PWhite(1.6,1), hpf=(PWhite(0,1000), PWhite(500,1500)), hpr=0.2)
d2 >> play("[{x }{ x}]", sample=2, amp=1, echo=0.3, hpf=PWhite(1000,2000), hpr=0.2, formant=(0, PWhite(0,10)))


d3 >> play("  O ", room=0.5, mix=0.2, amp=1.0)
d4.reset() >> play("X ", sample=2, amp=2)#, echo=0.2, hpf=PWhite(1000,2000), hpr=0.2)

b1 >> dirt(oct=5, amp=1, dur=8, sus=8, echo=0.1, formant=var([0,0.1,0.2,0.1,0.3,0],[1,1,1,1,1,1]))
b2 >> sawbass(PShuf([0,0,0,-1,2,4,2,1]), amp=PRand(P[0,3,3,3]), dur=0.5, sus=0.2, oct=7, cutoff=900, rq=0.2)


Master().lpf=300

k1 >> play("V(-i[--]-)", sample=0, amp=3)
b1 >> bass(0, dur=0.5, amp=P[0,1], oct=5, lpr=0.2, lpf=700)

Group(k1,b1).solo()
