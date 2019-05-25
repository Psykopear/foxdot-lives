FoxDot.start
FoxDot.midi(1)
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

Clock.midi_nudge = 0.3
a1 >> audioin(room=0.9, mix=(0.3,0.9))



p1.reset() >> midi(P[1,0])
p1.reset() >> MidiOut(P[0,0,0,0,1,2,-2,-1,-1,-1,1,-2,0].shuffle().mirror().mirror(), oct=4, dur=(1/3)*2, sus=0.2, amp=[1,1/2,1/2])

k1 >> play(P["x x x x [xx] [xx] x x"].shuffle().mirror().mirror(), hpr=0.1, hpf=100)
k2 >> play("(gt)h(h[hh])", sample=2, dur=(1/3)*2)
k3 >> play("X  ", sample=2, mix=(0,0.8), room=0.4, shape=(0,0.1))
d1 >> play(P["-*---=-*-vih--=t"].shuffle().mirror().mirror(), hpr=0.1, hpf=expvar([100,5000],16))
