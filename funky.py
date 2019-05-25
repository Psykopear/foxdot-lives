from FoxDot import *
Clock.clear()
Clock.bpm=150

funk_1 = {
    'dur': P[1,1,1,0.5,0.5, 0.5,0.5,1,1,1],
    'degree': P['x', 'x', 'h', ' ', 'x', ' ', 'x', ' ', 'h', ' '],
}

d1 >> play(**funk_1, sample=2)

