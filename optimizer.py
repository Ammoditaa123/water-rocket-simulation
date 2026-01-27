from simulator import runSimulation

def optimize(params, preassures, waterMasses):
    bHeight=0
    bConfig=None

    for p in preassures:
        for w in waterMasses:
            params["preassure"]=p
            params["totalMasses"]=params["dryMass"]+w
            sol=runSimulation(params)
            maxH=max(sol.y[1])

            if maxH>bHeight:
                bHeight=maxH
                bConfig=(p,w)

    return bConfig, bHeight