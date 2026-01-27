import numpy as np 
from scipy.integrate import solve_ivp
from physics import thrust, dragForce, G

def rocketDynamics(t, state, params):
    x, y, vx, vy, m = state

    if m<=params["dryMass"]:
        T=0
        mDot=0
    else:
        T=thrust(params["preassure"], params["nozzleArea"])
        mDot=-params["massFlow"]

    v=np.sqrt(vx**2 + vy**2)
    D=dragForce(v, params["cd"], params["area"])
    ax=-(D/m)*(vx/(v+1e-6))
    ay=(T-D*(vy/(v+1e-6))-m*G)/m

    return [vx, vy, ax, ay, mDot]

def runSimulation(params):
    state0=[0,0, params["v0x"], params["v0y"], params["totalMass"]]

    sol=solve_ivp(
        rocketDynamics, 
        [0,10], 
        state0, 
        args=(params,), 
        maxStep=0.01
    )
    return sol

