import streamlit as st
import numpy as np
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

st.set_page_config(page_title="Virtual IoT Sensor Lab", layout="wide")

# -----------------------
# PDF generator
# -----------------------
def generate_pdf(title, aim, materials, theory, procedure, observation, result, conclusion, applications):

    buffer = BytesIO()
    styles = getSampleStyleSheet()
    elements = []

    def add_section(heading, content):
        elements.append(Paragraph(f"<b>{heading}</b>", styles['Heading2']))
        elements.append(Spacer(1, 10))
        elements.append(Paragraph(content, styles['Normal']))
        elements.append(Spacer(1, 15))

    # Title
    elements.append(Paragraph(f"<b>{title}</b>", styles['Title']))
    elements.append(Spacer(1, 20))

    # Sections
    add_section("Aim", aim)
    add_section("Materials Required", materials)
    add_section("Theory", theory)
    add_section("Procedure", procedure)
    add_section("Observation", observation)
    add_section("Result", result)
    add_section("Conclusion", conclusion)
    add_section("Applications", applications)

    pdf = SimpleDocTemplate(buffer)
    pdf.build(elements)

    buffer.seek(0)
    return buffer

# -----------------------
# App Title
# -----------------------
st.title("🌐 Virtual IoT Sensor Laboratory")

lab = st.sidebar.selectbox(
    "Select Experiment",
    ["Temperature Sensor", "Soil Moisture Sensor", "Humidity Sensor"]
)

# =======================
# TEMPERATURE SENSOR
# =======================
if lab == "Temperature Sensor":

    st.header("🌡 Temperature Sensor Experiment")

    aim = "To study temperature monitoring using IoT sensors."

    materials = """DHT11 Sensor, Arduino/NodeMCU, Jumper wires,
Breadboard, Power supply, Computer"""

    theory = """Temperature sensors measure heat and convert it into electrical signals.
Used in IoT for weather monitoring, smart homes, and industries."""

    procedure = """1. Connect sensor to microcontroller
2. Power the system
3. Read temperature values
4. Display in app
5. Observe changes"""

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

    observation = "Temperature values vary and are plotted in graph."

    conclusion = "IoT temperature monitoring enables real-time tracking."

    applications = "Weather monitoring, Smart homes, Industrial systems"

    data = np.random.randn(20).cumsum() + temp
    st.line_chart(data)

    pdf = generate_pdf(
        "Temperature Sensor Experiment",
        aim, materials, theory, procedure,
        observation, result, conclusion, applications
    )

    st.download_button("📄 Download Report", pdf, "temperature_report.pdf")

# =======================
# SOIL MOISTURE SENSOR
# =======================
elif lab == "Soil Moisture Sensor":

    st.header("🌱 Soil Moisture Sensor Experiment")

    aim = "To study soil moisture monitoring using IoT."

    materials = """Soil Moisture Sensor, Arduino/NodeMCU,
Jumper wires, Breadboard, Power supply"""

    theory = """Soil moisture sensors measure water content in soil.
Used in smart irrigation systems."""

    procedure = """1. Insert sensor into soil
2. Connect to microcontroller
3. Power system
4. Read moisture values"""

    moisture = st.slider("Moisture (%)", 0, 100, 40)

    if moisture < 30:
        result = "Irrigation Required"
        st.error(result)
    else:
        result = "Moisture Level Normal"
        st.success(result)

    observation = "Moisture level changes and is shown in chart."

    conclusion = "Useful for automatic irrigation control."

    applications = "Agriculture, Smart irrigation systems"

    data = np.random.randn(20).cumsum() + moisture
    st.area_chart(data)

    pdf = generate_pdf(
        "Soil Moisture Sensor Experiment",
        aim, materials, theory, procedure,
        observation, result, conclusion, applications
    )

    st.download_button("📄 Download Report", pdf, "soil_moisture_report.pdf")

# =======================
# HUMIDITY SENSOR
# =======================
elif lab == "Humidity Sensor":

    st.header("💧 Humidity Sensor Experiment")

    aim = "To study humidity monitoring using IoT sensors."

    materials = """DHT11/DHT22 Sensor, Microcontroller,
Jumper wires, Breadboard, Power supply"""

    theory = """Humidity sensors measure moisture in air.
Used in weather stations and smart systems."""

    procedure = """1. Connect sensor
2. Power system
3. Read humidity values
4. Display in app"""

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

    observation = "Humidity varies and is visualized in graph."

    conclusion = "Helps maintain environmental comfort."

    applications = "Weather stations, Smart homes, Industries"

    data = np.random.randn(20).cumsum() + humidity
    st.line_chart(data)

    pdf = generate_pdf(
        "Humidity Sensor Experiment",
        aim, materials, theory, procedure,
        observation, result, conclusion, applications
    )

    st.download_button("📄 Download Report", pdf, "humidity_report.pdf")
