from FoxDot import *

Scale.default=Scale.phrygian

Clock.clear()

d1 >> play("-", dur=0.5, rate=4, shape=0.2, sample=PRand(list(range(5))), echo=0.1, amp=50, formant=PWhite(0,2)).solo()

b1 >> sawbass(var([0,3,2,1],[8]), oct=(4,5), amp=3.8, sus=4, dur=4)

k1 >> play("X ", sample=2, amp=20, shape=(0,0.2), room=0.4, mix=0.3)

Master().hpr=0.1;Master().hpf=0

s1 >> pluck(var([0,3,2,1],[8]), dur=PDur(3,8), sus=0.3, formant=(0,0.4), amp=0.3)
