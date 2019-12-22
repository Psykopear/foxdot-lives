from FoxDot import *

Clock.clear( )


Clock.bpm=160

s2 >> space(P[0,2,4,6,7,6,4,2], formant=P[0.9,0.1,0.2,0.3,0.4,0.5,0.6], room=0.3, mix=0.4)
b1 >> sawbass(var(P[(9,13),(0,7),(2,9),(0,7),(1,8),(2,9)], 32), dur=16, sus=16, amp=0.5)

k1 >> play("X ")

s1 >> pluck(oct=3)

