FoxDot.start
from FoxDot import *

Clock.clear()

Scale.default=Scale.phrygian
Root.default=var(P[0,-2,1,3], 16)
m = Master()


s1 >> feel(var([0,1,3],[12,2,2]), chop=P[4,2,1,3].shuffle().palindrome().shuffle().palindrome(), shape=0.2, room=0.5, mix=(0,1))
b1 >> evilbass(s1.degree, sus=0.3, dur=0.25, amp=(PEuclid(10,16)*0.3, 0.2), lpf=2690, mix=(0,1), room=0.7, lpr=0.2, oct=4)
d1 >> play("{=-p}", sample=PRand(list(range(8))), pan=PWhite(-0.8,0.8), dur=0.25, amp=PEuclid(9,16), mix=(0,1), room=1)
k1 >> play("X-", sample=2, amp=0.9)
d2 >> play("( h)(h )o( [hh])", sample=1, room=0.5, mix=0.3, amp=0.7, shape=(0,0.2))

m.hpf=1600;m.hpr=0.1;m.room=0.3;m.mix=0.3;

m.hpf=0;m.hpr=0;m.room=0;m.mix=0;
