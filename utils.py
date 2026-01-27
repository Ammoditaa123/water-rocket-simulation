import numpy as np

def deg_to_rad(deg):
    return np.deg2rad(deg)

def detectLanding(yArray):
    for i, y in enumerate(yArray):
        if y<=0 and i>0:
            return i
        
    return len(yArray)-1

def clamp(value, minVal, maxVal):
    return max(minVal, min(value, maxVal))