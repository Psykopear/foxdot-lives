Clock.clear()

from FoxDot import *
Scale.default=Scale.locrian
Root.default=var(P[0], 1)
Root.default=var([0,0,0,0,0,0,0,-0]+P[-0,0,0,0].shuffle().mirror(),[4,4,4,4,2,2,2,2])


s1 >> klank(
    b1.degree,
    chop=2,
    shape=(0,0.2),
    formant=(0.3,0),
    amp=0.4,
)

s2 >> sitar(
    b1.degree + PRand([0,0,0,0,1,2,3,4]),
    # 0,
    root=0,
    dur=1/4,
    amp=PEuclid(P[9,7,5,3].shuffle().mirror(),11)*0.9,
    sus=0.3,
    oct=(4, 5),
    hpr=0.4,
    hpf=sinvar([0,4000],dur=1/16),
    bpr=0,
    bpf=0,#sinvar([100,3000],dur=16)
)


b1 >> evilbass(
    # 0,
    degree=P[0,0,4,0,1,2,-3].shuffle().palindrome(),
    sus=0.5,
    dur=1/4,
    amp=PEuclid(5,11).shuffle()*0.5,
    oct=4,
    root=0,
)

(
    k1 >> play(
        # P["X-X-X(---[-X])(X-X)(XX-)"].amen(),
        P["X-"],
        sample=2,
        amp=3,
        chop=0
    ).every(8,'stutter',PRand([1,2,4])),
    d1 >> play(
        "(- [--] )( [--]- )o([--] - )( [--]- )",
        room=(0,0.8),
        mix=(0,0.5),
        sample=(2, PRand(list(range(8)))),
        echo=(0,PRand([0.02,0.03,0.04])),
        amp=0,
    )
)



m = Master()
m.hpf=600;m.hpr=0.3;m.room=0.2;m.mix=0.2;
m.amplify=var([1,1,1,1],[1/4])


Clock.bpm=142


(
)

k2 >> play("X--", dur=1/3, sample=2, shape=(0,0.1), formant=(0,0.1), amp=(1.0,0.5)),
b2 >> evilbass(0, dur=1/3, amp=PEuclid(7,12)*1.5, sus=0.6),
d3 >> play(
    "tn-",
    echo=sinvar([0.1,0.3]),
    pan=(sinvar([-0.8,0.8]),sinvar([0.8,-0.8])),
    room=0.6,
    mix=0.3,
    shape=(0,0.3),
    formant=(0,0.5),
    dur=1/6,
    amp=PEuclid(PRand([7,9,11,8,10]), 12),
    chop=3,
    pshift=sinvar([0,60], 16),
)
