from FoxDot import *

Scale.default=Scale.phrygian

Clock.clear()

s1 >> sitar(var([0,1,2,1,3],[8,8,8,4,4]) + PRand([0,0,0,0,1,2,3,4]), dur=PDur(P[4,5,6,7].shuffle(), var([8,11],[8])), sus=sinvar([0.2,0.5],16), amp=0.5, oct=((4,5),5), chop=(0,2), mix=(0.2,0.8), room=0.4)
b1 >> bass(s1.degree, dur=PDur(3,8), sus=0.2, amp=0.5, lpf=sinvar([200,900],16), lpr=0.05)
k1 >> play("{[ff]f }", echo=0.5, rate=PRand([1]))
