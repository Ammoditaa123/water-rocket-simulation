import numpy as np

G=9.81
RHO_water=1000
RHO_air=1.225

def thrust(preassure, nozzleArea):
    return preassure*nozzleArea

def massFlowRate(preassure, nozzleArea):
    return nozzleArea*np.sqrt(2*preassure/RHO_water)

def dragForce(v, cd, area):
    return 0.5*RHO_air*cd*area*v**2
