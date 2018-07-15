from FoxDot import * 

k1 >> play("X-", amp=4)

s1 >> play("O   ", amp=0.2, room=0.1, size=0.1)
h1 >> play("-  {[--]-}  --  ")
c1 >> play("=               ")

Scale.default = Scale.phrygian
print(dir(Scale))
print(SynthDefs)

Clock.clear()
Clock.stop()

Clock.bpm = 134

b1 >> bass(P[0, 0, PRand([0]*10+[2,-1,0,1])], dur=Fraction(1,4), sus=0.2, lpf=2000, lpr=0.2, amp=[0,1,1,0, 0.5,1,0,1, 0,1,1,0, 0.5,1,1,0])

n1 >> sitar(PRand([b1.degree]*8+[b1.degree + 1, b1.degree + 2, b1.degree + 3]), oct=6, dur=0.5, sus=0.6, amp=0.4, hpf=linvar([100, 1000], 32), chop=3)

n1.stop()

g1 >> zap((b1.degree, b1.degree + 0.1)+PRand([0,1]), oct=5, dur=Fraction(1, 2), sus=2, amp=PRand([0.2, 0.3, 0.5]), chop=6, shape=PRand([0.6, 0.3, 0.5, 0.4]))

g1.hpf=linvar([0, 5000], 32)
g1.hpr=0.1

Group(k1, s1, h1, c1).amplify=var([1, 0], [28, 4])

k1.amplify=1



print(SynthDefs)


a1 >> varsaw((0, 0.01, 3), dur=32, sus=32, oct=(3,4), amp=0.8)

d1 >> play("X  [--]", sample=3)

b1 >> dub([0,0,0,3])
