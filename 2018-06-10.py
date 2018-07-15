from FoxDot import *
FoxDot.start
Scale.default=Scale.phrygian
Clock.clear()
tempo = Player()
tempo >> pluck(amp=0)
tempo.dur=Fraction(1,2)
tempo.degree=P[0,0,0,1,2,3,4,5,0,0,3,4,6,0,1,2].shuffle().mirror()
t = { 'dur': tempo.dur }




s1 >> klank(P[0,1,2,3,4,5,0,0,3,4].shuffle().mirror().amen(), chop=4, dur=1, amp=1)
s2 >> pluck(s1.degree, formant=(0,PWhite(0,1)), shape=(0,PWhite(0,0.3)), pan=(PWhite(-0.8,0.8), PWhite(0.8,-0.8)), dur=1/4, dist=0.2, amp=0.1)
b1 >> evilbass(s1.degree, dur=0.25, sus=1, amp=PEuclid(P[4,5,6,7].shuffle().mirror(), 8)*4)
k1 >> play("X[ ]", sample=2, amp=4)
d2 >> play("  O ")
d1 >> play("-", sample=PRand(list(range(5))), amp=PEuclid(P[12,10,7,13].mirror().shuffle(), 16)*2, )


Master().dur=Fraction(1,2)

g = Group(d1, d2, k1, b1)
g.solo();g.hpf=0;g.hpr=0.3;g.room=0.3;g.mix=0.3;


from FoxDot import P
class Q(P):
    def __getitem__(self, *args, **kwargs):
        return super().__getitem__(*args, **kwargs).shuffle().mirror()
