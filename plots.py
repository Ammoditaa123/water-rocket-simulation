import streamlit as st
import pandas as pd
import time
from utils import detectLanding

def plotResults(sol):
    t=sol.t
    x, y, vx, vy, m = sol.y
    landing_idx=detectLanding(y)

    x=x[:landing_idx]
    y=y[:landing_idx]
    t=t[:landing_idx]
    vx=vx[:landing_idx]
    vy=vy[:landing_idx]

    df=pd.DataFrame({
        "time":t, 
        "x":x, 
        "y":y, 
        "velocity":(vx**2 +vy**2)**0.5
    })

    st.subheader("Height vs Time")
    st.line_chart(df.set_index("time")[["y"]], height=300)

    st.subheader("Velocity vs Time")
    st.line_chart(df.set_index("time")[["velocity"]], height=300)

    return df

def trajectory(df, speed):
    st.subheader("Trajectory Animation")
    placeholder=st.empty()
    trailX=[]
    trailY=[]
    
    for i in range(len(df)):
        trailX.append(df["x"].iloc[i])
        trailY.append(df["y"].iloc[i])

        plotdf=pd.DataFrame({
            "x":trailX,
            "y":trailY
        })

        placeholder.line_chart(plotdf.set_index("x"))
        time.sleep(speed)


