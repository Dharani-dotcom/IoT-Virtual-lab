mport streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Virtual IoT Sensor Lab", layout="wide")

# -----------------------
# Custom CSS
# -----------------------
st.markdown("""
<style>

.main-title{
font-size:45px;
font-weight:bold;
text-align:center;
background: linear-gradient(90deg,#00C9FF,#92FE9D);
-webkit-background-clip:text;
color:transparent;
}

.card{
padding:20px;
border-radius:15px;
background-color:#f5f7fa;
box-shadow:0px 4px 20px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🌐 Virtual IoT Sensor Laboratory</p>', unsafe_allow_html=True)

# -----------------------
# Sidebar
# -----------------------
st.sidebar.title("🧪 Experiments")

lab = st.sidebar.radio(
"Select Sensor",
[
"Temperature Sensor",
"Soil Moisture Sensor",
"Humidity Sensor",
"Gas Sensor",
"Light Sensor",
"Motion Sensor"
]
)

# -----------------------
# Temperature Sensor
# -----------------------
if lab == "Temperature Sensor":

    st.header("🌡 Temperature Monitoring")

    col1,col2 = st.columns(2)

    with col1:
        temp = st.slider("Temperature (°C)",-10,50,25)

        if temp > 35:
            st.error("🔥 High Temperature")
        elif temp < 10:
            st.warning("❄ Cold Environment")
        else:
            st.success("Normal Temperature")

    with col2:

        data = np.random.randn(20).cumsum() + temp
        st.line_chart(data)

# -----------------------
# Soil Moisture
# -----------------------
elif lab == "Soil Moisture Sensor":

    st.header("🌱 Smart Irrigation Sensor")

    col1,col2 = st.columns(2)

    with col1:

        moisture = st.slider("Soil Moisture (%)",0,100,40)

        if moisture < 30:
            st.error("💧 Irrigation Needed")
        else:
            st.success("Soil Moisture OK")

    with col2:

        data = np.random.randn(20).cumsum() + moisture
        st.area_chart(data)

# -----------------------
# Humidity
# -----------------------
elif lab == "Humidity Sensor":

    st.header("💧 Humidity Monitoring")

    humidity = st.slider("Humidity (%)",0,100,50)

    if humidity > 80:
        st.warning("High Humidity")
    elif humidity < 30:
        st.warning("Low Humidity")
    else:
        st.success("Comfort Level")

    data = np.random.randn(20).cumsum() + humidity
    st.line_chart(data)

# -----------------------
# Gas Sensor
# -----------------------
elif lab == "Gas Sensor":

    st.header("🧪 Gas Leak Detection")

    gas = st.slider("Gas Level (ppm)",0,1000,100)

    if gas > 400:
        st.error("⚠ Gas Leak Detected")
    else:
        st.success("Safe Air")

    data = np.random.randn(20).cumsum() + gas
    st.line_chart(data)

# -----------------------
# Light Sensor
# -----------------------
elif lab == "Light Sensor":

    st.header("💡 Smart Light Sensor")

    light = st.slider("Light Intensity",0,100,60)

    if light < 30:
        st.info("Street Lights ON")
    else:
        st.info("Street Lights OFF")

    data = np.random.randn(20).cumsum() + light
    st.line_chart(data)

# -----------------------
# Motion Sensor
# -----------------------
elif lab == "Motion Sensor":

    st.header("🚶 Motion Detection System")

    motion = st.selectbox("Motion Detected?",["No","Yes"])

    if motion == "Yes":
        st.warning("🚨 Motion Detected")
    else:
        st.success("Area Secure")
