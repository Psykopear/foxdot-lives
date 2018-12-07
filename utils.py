def drange(start, end, step=0.1):
    """
    Return a list of floats from 
    start to end with the given step
    list(drange(0,0.2)) == [0.0,0.1,0.2]
    """
    r = start
    while r <= end:
        yield r
        r += step
