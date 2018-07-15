from FoxDot import *
# Just a dummy synth used to keep tempo fractions
tempo = Player()
tempo >> pluck(amp=0)
tempo.dur = Fraction(1,2)
t = {'dur': tempo.dur}
# Set default scale
Scale.default=Scale.phrygian
# Create live file
