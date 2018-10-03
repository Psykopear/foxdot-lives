FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()

Root.default=var((PIndex()*4)%7,32)

(
)
    s2 >> sitar(var([0,1,2,-1], PRand([1,2,4])), dur=PDur(3,8), oct=(4,5), amp=0.8, sus=0.3).penta().sometimes('splice', 4, dur=3)
    b1 >> sawbass(s2.degree, sus=0.2, dur=1/4, amp=PEuclid(11,16))
    k1 >> play("|X2|-").every(6, 'stutter', 4, dur=3).sometimes('stutter', 3)
    d1 >> play("=-*-", sample=2, room=0.3, mix=0.3).sometimes('stutter', 4, dur=3)
    s1 >> klank(0, dur=4, chop=16, formant=(sinvar([0,4],16),0), shape=(0,sinvar(0.1,0.5)), room=0.5, mix=0.4).spread()
