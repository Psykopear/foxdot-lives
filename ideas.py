Scale.default=Scale.phrygian
b1 >> evilbass(var([0,0,3,1,-1], [4,4,4,2,2]), dur=PRand([0.5,0.25]), sus=s1.dur, shape=(0,0.2))
k1 >> play("x-", sample=5, echo=(0,0.25), amp=(1,0.2), hpr=0.3, hpf=(0,PWhite(200,1000)))
