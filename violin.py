Scale.default.set(Scale.minorPentatonic)

Scale.


f1 >> nylon(b1.degree, dur=16,oct=4,room=1, amp=1.5).every(5, 'stutter', 4, cycle=8)



d1 >> play("s", sample=PRand([1,2,3,1,1,1,1]), amp=[1,0.8])
d2 >> play("p      t    p ", sample=PRand([1,2,3]))
d3 >> play("o  ", sample=3,amp=0.2,room=1)

k1 >> play("X X X X{ [xx] }", sample=3, amp=2)

Group(d2,d3,k1,b1).amplify=var([1,0], [28,4])

b1 >> bass(PRand([PRand([0,1,2,3]), P[3,0,0,1, 0,0,0,0, 2,0,0,0, 0,0,1,0]]), amp=P[0,0.5,1,0, 0,1,0,1, 0,1,1,0, 0.5,0,1,0], dur=Fraction(1,4), sus=0.2)
s1 >> viola(P[0, PRand([2,1,0]), PRand([2,3]), PRand([2,5])] + b1.degree, dur=PRand([2,0.5,1,0.25]), shape=0.5, bpf=linvar([100, 10000], 32))


print(SynthDefs)
