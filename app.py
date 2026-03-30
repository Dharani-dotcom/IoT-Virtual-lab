import streamlit as st
import pandas as pd
import numpy as np
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

st.set_page_config(page_title="Virtual IoT Sensor Lab", layout="wide")

# -----------------------
# PDF generator
# -----------------------
def generate_pdf(title, aim, theory, result):

    buffer = BytesIO()
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph(f"<b>{title}</b>", styles['Title']))
    elements.append(Spacer(1,20))

    elements.append(Paragraph(f"<b>Aim:</b> {aim}", styles['Normal']))
    elements.append(Spacer(1,10))

    elements.append(Paragraph(f"<b>Theory:</b> {theory}", styles['Normal']))
    elements.append(Spacer(1,10))

    elements.append(Paragraph(f"<b>Result:</b> {result}", styles['Normal']))

    pdf = SimpleDocTemplate(buffer)
    pdf.build(elements)

    buffer.seek(0)

    return buffer

# -----------------------
# Title
# -----------------------

st.title("🌐 Virtual IoT Sensor Laboratory")

# Sidebar
lab = st.sidebar.selectbox(
"Select Experiment",
[
"Temperature Sensor",
"Soil Moisture Sensor",
"Humidity Sensor"
]
)

# -----------------------
# Temperature Sensor
# -----------------------

if lab == "Temperature Sensor":

    aim = "To study temperature monitoring using IoT sensors."

    theory = """
Temperature sensors measure environmental heat and convert it into electrical signals.
In IoT systems these sensors help monitor weather, industrial machines,
and smart homes.
"""

    st.header("🌡 Temperature Sensor Experiment")

    st.subheader("Aim")
    st.write(aim)

    st.subheader("Theory")
    st.write(theory)

    temp = st.slider("Temperature (°C)",-10,50,25)

    if temp > 35:
        result = "High Temperature Detected"
        st.error(result)
    elif temp < 10:
        result = "Low Temperature Detected"
        st.warning(result)
    else:
        result = "Normal Temperature"
        st.success(result)

    data = np.random.randn(20).cumsum() + temp
    st.line_chart(data)

    # Quiz
    st.subheader("Quiz")

    q1 = st.radio(
    "Which sensor is commonly used for temperature monitoring?",
    ["LDR","DHT11","MQ2"]
    )

    if st.button("Submit Quiz"):

        if q1 == "DHT11":
            st.success("Correct Answer ✅")
        else:
            st.error("Wrong Answer ❌")

    # PDF Download

    pdf = generate_pdf(
        "Temperature Sensor Experiment",
        aim,
        theory,
        result
    )

    st.download_button(
        label="📄 Download Experiment Report",
        data=pdf,
        file_name="temperature_lab_report.pdf",
        mime="application/pdf"
    )

# -----------------------
# Soil Moisture
# -----------------------

elif lab == "Soil Moisture Sensor":

    aim = "To study soil moisture monitoring in smart agriculture."

    theory = """
Soil moisture sensors measure water content in soil.
They are widely used in IoT based irrigation systems
to automate watering for crops.
"""

    st.header("🌱 Soil Moisture Sensor")

    st.subheader("Aim")
    st.write(aim)

    st.subheader("Theory")
    st.write(theory)

    moisture = st.slider("Moisture (%)",0,100,40)

    if moisture < 30:
        result = "Irrigation Required"
        st.error(result)
    else:
        result = "Moisture Level Normal"
        st.success(result)

    data = np.random.randn(20).cumsum() + moisture
    st.area_chart(data)

    # Quiz

    st.subheader("Quiz")

    q1 = st.radio(
    "Which field mainly uses soil moisture sensors?",
    ["Agriculture","Networking","Robotics"]
    )

    if st.button("Submit Quiz"):

        if q1 == "Agriculture":
            st.success("Correct Answer ✅")
        else:
            st.error("Wrong Answer ❌")

    pdf = generate_pdf(
        "Soil Moisture Sensor Experiment",
        aim,
        theory,
        result
    )

    st.download_button(
        label="📄 Download Experiment Report",
        data=pdf,
        file_name="soil_moisture_lab_report.pdf",
        mime="application/pdf"
    )

# -----------------------
# Humidity Sensor
# -----------------------

elif lab == "Humidity Sensor":

    aim = "To understand humidity monitoring using IoT sensors."

    theory = """
Humidity sensors measure moisture present in air.
These sensors are widely used in weather monitoring
and smart homes.
"""

    st.header("💧 Humidity Sensor")

    st.subheader("Aim")
    st.write(aim)

    st.subheader("Theory")
    st.write(theory)

    humidity = st.slider("Humidity (%)",0,100,50)

    if humidity > 80:
        result = "High Humidity"
        st.warning(result)
    elif humidity < 30:
        result = "Low Humidity"
        st.warning(result)
    else:
        result = "Comfort Level"
        st.success(result)

    data = np.random.randn(20).cumsum() + humidity
    st.line_chart(data)

    # Quiz

    st.subheader("Quiz")

    q1 = st.radio(
    "Humidity sensors measure:",
    ["Air moisture","Light intensity","Sound"]
    )

    if st.button("Submit Quiz"):

        if q1 == "Air moisture":
            st.success("Correct Answer ✅")
        else:
            st.error("Wrong Answer ❌")

    pdf = generate_pdf(
        "Humidity Sensor Experiment",
        aim,
        theory,
        result
    )

    st.download_button(
        label="📄 Download Experiment Report",
        data=pdf,
        file_name="humidity_lab_report.pdf",
        mime="application/pdf"
    )
