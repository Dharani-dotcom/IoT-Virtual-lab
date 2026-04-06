import streamlit as st
import numpy as np
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

st.set_page_config(page_title="Virtual IoT Sensor Lab", layout="wide")

# -----------------------
# PDF generator (UPDATED)
# -----------------------
def generate_pdf(title, aim, materials, theory, procedure, observation, result, conclusion, applications):

    buffer = BytesIO()
    styles = getSampleStyleSheet()
    elements = []

    def section(title, content):
        elements.append(Paragraph(f"<b>{title}</b>", styles['Heading2']))
        elements.append(Spacer(1, 10))
        elements.append(Paragraph(content, styles['Normal']))
        elements.append(Spacer(1, 15))

    # Title
    elements.append(Paragraph(f"<b>{title}</b>", styles['Title']))
    elements.append(Spacer(1, 20))

    # Sections
    section("Aim", aim)
    section("Materials Required", materials)
    section("Theory", theory)
    section("Procedure", procedure)
    section("Observation", observation)
    section("Result", result)
    section("Conclusion", conclusion)
    section("Applications", applications)

    pdf = SimpleDocTemplate(buffer)
    pdf.build(elements)

    buffer.seek(0)
    return buffer

# -----------------------
# Title
# -----------------------

st.title("🌐 Virtual IoT Sensor Laboratory")

lab = st.sidebar.selectbox(
    "Select Experiment",
    ["Temperature Sensor", "Soil Moisture Sensor", "Humidity Sensor"]
)

# -----------------------
# Temperature Sensor
# -----------------------

if lab == "Temperature Sensor":

    aim = "To study temperature monitoring using IoT sensors."

    materials = "DHT11 Sensor, Arduino/NodeMCU, Jumper wires, Breadboard, Power supply, Computer"

    theory = """Temperature sensors measure heat and convert it into electrical signals.
Used in IoT for weather monitoring, smart homes, and industries."""

    procedure = """1. Connect sensor to microcontroller.
2. Power the system.
3. Read temperature values.
4. Display in app.
5. Observe using slider."""

    st.header("🌡 Temperature Sensor")

    temp = st.slider("Temperature (°C)", -10, 50, 25)

    if temp > 35:
        result = "High Temperature Detected"
        st.error(result)
    elif temp < 10:
        result = "Low Temperature Detected"
        st.warning(result)
    else:
        result = "Normal Temperature"
        st.success(result)

    observation = "Temperature varies and is displayed as a graph."

    conclusion = "IoT temperature monitoring is effective for real-time applications."

    applications = "Weather systems, Smart homes, Industry"

    data = np.random.randn(20).cumsum() + temp
    st.line_chart(data)

    pdf = generate_pdf(
        "Temperature Sensor Experiment",
        aim, materials, theory, procedure,
        observation, result, conclusion, applications
    )

    st.download_button("📄 Download Report", pdf, "temperature.pdf")

# -----------------------
# Soil Moisture Sensor
# -----------------------

elif lab == "Soil Moisture Sensor":

    aim = "To study soil moisture monitoring using IoT."

    materials = "Soil Moisture Sensor, Arduino, Wires, Breadboard, Power supply"

    theory = """Measures water content in soil.
Used in smart irrigation systems."""

    procedure = """1. Insert sensor into soil.
2. Connect to controller.
3. Power system.
4. Monitor readings."""

    st.header("🌱 Soil Moisture Sensor")

    moisture = st.slider("Moisture (%)", 0, 100, 40)

    if moisture < 30:
        result = "Irrigation Required"
        st.error(result)
    else:
        result = "Moisture Normal"
        st.success(result)

    observation = "Moisture level changes based on input."

    conclusion = "Helps automate irrigation efficiently."

    applications = "Agriculture, Smart irrigation"

    data = np.random.randn(20).cumsum() + moisture
    st.area_chart(data)

    pdf = generate_pdf(
        "Soil Moisture Sensor Experiment",
        aim, materials, theory, procedure,
        observation, result, conclusion, applications
    )

    st.download_button("📄 Download Report", pdf, "soil.pdf")

# -----------------------
# Humidity Sensor
# -----------------------

elif lab == "Humidity Sensor":

    aim = "To study humidity monitoring using IoT."

    materials = "DHT11 Sensor, Microcontroller, Wires, Breadboard"

    theory = """Humidity sensors measure moisture in air.
Used in weather and smart systems."""

    procedure = """1. Connect sensor.
2. Power system.
3. Read humidity.
4. Display values."""

    st.header("💧 Humidity Sensor")

    humidity = st.slider("Humidity (%)", 0, 100, 50)

    if humidity > 80:
        result = "High Humidity"
        st.warning(result)
    elif humidity < 30:
        result = "Low Humidity"
        st.warning(result)
    else:
        result = "Comfort Level"
        st.success(result)

    observation = "Humidity varies with environment."

    conclusion = "Useful for environmental monitoring."

    applications = "Weather stations, Homes, Industry"

    data = np.random.randn(20).cumsum() + humidity
    st.line_chart(data)

    pdf = generate_pdf(
        "Humidity Sensor Experiment",
        aim, materials, theory, procedure,
        observation, result, conclusion, applications
    )

    st.download_button("📄 Download Report", pdf, "humidity.pdf")
