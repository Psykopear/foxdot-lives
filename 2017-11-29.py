from FoxDot import *

a1 >> prophet((0,2,4,6,var([7,9,8],8)), chop=1, scale=Scale.lydianMinor, amp=1, oct=5, dur=.25, attack=.1, cutoff=0, room=0.4, mix=0.2)

b1 >> sawbass(PRand([0,7,8,9]), scale=Scale.lydianMinor, amp=P[0,1,1,1, 0,1,1,1, 0,1,1,1, 0,1,0,1]*2, sus=0.1, oct=5, dur=0.25, rq=0.1, cutoff=500)
d1 >> play("<V ><= -{[--] -}><  o >")

Group(a1).solo()
