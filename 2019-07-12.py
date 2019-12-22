from FoxDot import *


Clock.bpm=160


Clock.clear()

a1 >> audioin(2, amp=1, room=0, mix=0)

s1 >> space(P[0,2,4,6,7,6,4,2], pan=sinvar([-1,1], 16), chop=4, formant=P[0,0.1,0.2,0.3,0.4], shape=0.2, amp=1)

b1 >> evilbass(var([(9,13),(0,7),(2,9),(0,7),(1,8),(2,9)],32), dur=PDur(P[3,4,5],8), sus=0.6, amp=0.2, oct=(4), chop=(0))

k1 >> play("XhXh", sample=2, amp=0.3).sometimes("stutter", 3, dur=1).sometimes("amen")
