import math
def BallVolume(h,r=10):

    volume =  ((4 * math.pi * r**3))/3 - ((math.pi * h**2 * (3*r - h))/3)
    return (volume)


print (BallVolume(2))