from FoxDot import *

print(SynthDefs)

a1 >> pads(sus=0.3, oct=3)
a1.reset() >> dab()
a1.reset() >> varsaw()
a1.reset() >> lazer(sus=0.2, oct=3)
a1.reset() >> growl()
a1.reset() >> bass()
a1.reset() >> dirt()
a1.reset() >> crunch()
a1.reset() >> rave()
a1.reset() >> scatter()
a1.reset() >> charm()
a1.reset() >> bell()
a1.reset() >> gong()
a1.reset() >> soprano(sus=0.3, oct=3)
a1.reset() >> dub()
a1.reset() >> viola(oct=3)
a1.reset() >> scratch()
a1.reset() >> klank()
a1.reset() >> ambi()

for i in SynthDefs:
    print(f'a1.reset() >> {i}()')

a1.reset() >> audioin()
a1.reset() >> pads()
a1.reset() >> noise()
a1.reset() >> dab()
a1.reset() >> varsaw()
a1.reset() >> lazer()
a1.reset() >> growl()
a1.reset() >> bass()
a1.reset() >> dirt()
a1.reset() >> crunch()
a1.reset() >> rave()
a1.reset() >> scatter()
a1.reset() >> charm()
a1.reset() >> bell()
a1.reset() >> gong()
a1.reset() >> soprano()
a1.reset() >> dub()
a1.reset() >> viola()
a1.reset() >> scratch()
a1.reset() >> klank()
a1.reset() >> ambi()
a1.reset() >> glass()
a1.reset() >> soft(sus=0.2, rate=1)
a1.reset() >> quin(oct=4)
a1.reset() >> pluck(oct=3, sus=0.4, amp=2)
a1.reset() >> spark(oct=3)
a1.reset() >> blip()
a1.reset() >> ripple()
a1.reset() >> creep()
a1.reset() >> orient(oct=3)
a1.reset() >> zap(oct=3)
a1.reset() >> marimba()
a1.reset() >> fuzz()
a1.reset() >> bug(oct=3, sus=0.5)
a1.reset() >> pulse(P[0,0,1,0], dur=0.25, oct=4, sus=0.2)
a1.reset() >> saw(oct=3, lpf=linvar(10000,100,0.25), sus=0.4)
a1.reset() >> snick()
a1.reset() >> twang()
a1.reset() >> karp(oct=4, sus=0.2, dur=0.25)
a1.reset() >> arpy(oct=4)
a1.reset() >> nylon(oct=4)
k1.reset() >> donk(0, amp=1, oct=3, sus=1, shape=(0,0.5), formant=(0,0.1)).solo()
b1.reset() >> sawbass(amp=P[1,1,1, 1,1,1, 1,1,1, 1,1,1]*3, dur=Fraction(1,3), sus=0.2, cutoff=1000, lpr=0.3, lpf=PWhite(200,5200), rq=0.2, hpf=0, hpr=0.1)
k1.reset() >> play("<X><[ --]>",  sample=2, amp=1.2, dur=1, hpf=0, hpr=0.1, formant=0)
k2 >> play("  ")

a1.reset() >> squish()
a1.reset() >> swell((0,2), chop=4, amp=2, shape=PWhite(0,0.8), formant=a1.shape, sus=1, echo=0.1, oct=(4,5))
a1.reset() >> razz()
a1.reset() >> star()
s1.reset() >> piano(oct=3)
a1.reset() >> prophet(oct=5)

d1 >> play("-", dur=0.25, echo=PRand([0.5,0.1,2]), amp=PWhite(0.2,1.2), formant=(PWhite(0,1), PWhite(0,2)), sample=PRand([0,1,2,3,4]), hpr=0.2, hpf=(PWhite(100,1000), PWhite(200,2000)))
d2 >> play("  O ", room=0.2, mix=0.2, amp=0.7)
s2.reset() >> sitar(chop=3, hpf=PWhite(100,3000), hpr=0.2, formant=PWhite(0,2), echo=0, pan=PWhite(-1,1), amp=0.6)

# Up with bpms
Clock.bpm=144
Root.default=var([5,5,8,7,10],[4,4,4,2,2])


Master().hpf=800; Master().hpr=0.9; Master().formant=PWhite(0, 0.4); Master().mix=0.3; Master().room=0.3;

k2.reset() >> play("<X({ [--]-} h)>< yO( o)>", sample=2, amp=1.2, shape=0)
k2.reset() >> play("X ", sample=2, amp=1)
b2.reset() >> sawbass(sus=0.35, amp=P[0,2], oct=(4,5), dur=PRand([0.25,0.5]), shape=0, rq=0.2)
s3.reset() >> sitar(amp=2, chop=4, oct=5, formant=var([0,1,0.5,2,1],[8,4,4,4,4]), shape=var([0,0.4], [28,4])).every(4, 'stutter', 2)

Group(k2,b2,s3).solo()


from FoxDot import *
Clock.bpm=130
Root.default=5
b1.reset() >> evilbass(var([0,0,0,2,1],[4,4,4,2,2]), scale=Scale.locrian, dur=PRand([0.5,0.25]), sus=0.6, amp=P[1,0,1,1, 1,0,1,0, 0,1,1,1, 1,0,1,1]*4)
k2.reset() >> play("< ({ [--]-} h)>< yO( o)>", sample=2, amp=(1.5,1.2), hpf=linvar([100,2000],16), hpr=0.2)
k1 >> play("x ", chop=0, sample=5, amp=2, shape=(0,0.2))
s1 >> pluck(b1.degree, dur=PRand([0.25,0.5]), shape=(PWhite(0, 0.2),PWhite(0, 0.3)), amp=4.5, formant=PRand([0,0.2,0.3,0.1]), scale=Scale.locrian, lpf=0, chop=1, hpf=(PWhite(100,2000), PWhite(100,2000)), hpr=0.2)
k2.reset() >> play("  ", sample=2, amp=1)


from FoxDot import *
s1 >> play("- h ")
Clock.set_time(0)

def tap_tempo():
    input("Start pressing enter")
    first = time.time()
    input("")
    second = time.time()
    input("")
    third = time.time()
    input("")
    fourth = time.time()
    Clock.set_time(0)
    bpm = 1 / (sum([fourth - third, third - second, second - first]) / 4.0) * 60
    Clock.bpm=bpm
    print("Set to %s bpms" % bpm)

def nudge(back=False):
    if not back:
        Clock.nudge+=0.05
    else:
        Clock.nudge-=0.05

nudge()
nudge('backwards')
tap_tempo()
