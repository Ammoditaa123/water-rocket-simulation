import streamlit as st
import numpy as np
from simulator import runSimulation
from plots import plotResults, trajectory
from optimizer import optimize
from utils import deg_to_rad

st.set_page_config(page_title="WATER ROCKET SIMULATION", layout="wide")
st.title("Interactive Water Rocket Simulation")
preassure=st.sidebar.slider("Preassure (Pa)", 200000, 800000, 400000)
angle=st.sidebar.slider("Launch Angle (deg)", 30, 90, 45)
waterMass=st.sidebar.slider("Water Mass (kg)", 0.2, 1.5, 1.0)
theta=deg_to_rad(angle)

params={
    "preassure":preassure,
    "nozzleArea":1e-4,
    "cd":0.5,
    "area":0.01,
    "dryMass":0.2,
    "totalMass":0.2+waterMass,
    "massFlow":0.05,
    "v0x":0,
    "v0y":0
}

tab1, tab2 = st.tabs(["Simulation", "Optimization"])

with tab1:
    sol=runSimulation(params)
    df=plotResults(sol)
    st.markdown("---")
    st.subheader("Animation Controls")

    speed=st.slider(
        "String",
        min_value=0.01,
        max_value=0.2,
        value=0.05,
        step=0.01
    )
    if st.button("Play Trajectory Animation"):
        trajectory(df, speed)

    st.download_button("Download CSV", df.to_csv(), "rocketData.csv")

with tab2:
    if st.button("Find Optimal Configuration"):
        best, height = optimize(
            params, 
            preassures= range(200000, 800000, 100000),
            waterMasses=[0.5, 1.0, 1.5]
        )
        st.success(f"Best Preassure: {best[0]} Pa | Water Mass: {best[1]} kg")





        