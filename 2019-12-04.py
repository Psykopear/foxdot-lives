#XXX
from FoxDot import *

# Reggae
Clock.bpm=70
Scale.default=Scale.aeolian
d1 >> play("  x ", dur=0.5, sample=2, amp=2)
d2 >> play("--", sample=PRand(list(range(2))), amp=var([0.5,1],0.5), room=var([0.2,1],0.5), mix=(0,1), dur=0.5).often("stutter", 3)
d3 >> play("   =        ", dur=0.5, sample=1, mix=(0,1), room=(1), shape=0.2, formant=0, hpf=200)
b3 >> dbass(PChain({0: [4,5], 4: [6], 6: [4,0], 5: [6,4] }), dur=PDur(12, 16), amp=P[0,PRand([0,1,1,1,1,1])]*0.8, oct=4, delay=P[0.05,0.08,0.04,0.03,0.01,0.00]*PRand([0,0.5,0.5,0.5,0.5]))
s2 >> sitar((b2.degree, b1.degree + 2, b1.degree + 3) + PRand([0,0,0,0,3]), dur=PDur(1,4), delay=0.5, amp=0.6, strum=0.02, sus=0.3, mix=0.3, room=0.3).often("stutter", 3, mix=(0,1))
