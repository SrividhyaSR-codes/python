import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Calculator + BMI Calculator",
    page_icon="🧮",
    layout="centered"
)

# Title
st.title("🧮 Streamlit Calculator & BMI Calculator")

st.write("Perform basic mathematical operations or calculate your Body Mass Index (BMI).")

# Main calculator section
st.header("Calculator")
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)
operation = st.selectbox(
    "Choose Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            st.error("Division by zero is not allowed.")
            st.stop()
        result = num1 / num2

    st.success(f"Result = {result}")

st.markdown("---")

# BMI calculator section
st.header("BMI Calculator")
unit_system = st.selectbox("Choose unit system", ["Metric (kg, cm)", "Imperial (lb, in)"])

if unit_system == "Metric (kg, cm)":
    weight_input = st.text_input("Weight (kg)", value="", placeholder="e.g. 70")
    height_input = st.text_input("Height (cm)", value="", placeholder="e.g. 175")
else:
    weight_input = st.text_input("Weight (lb)", value="", placeholder="e.g. 154")
    height_input = st.text_input("Height (in)", value="", placeholder="e.g. 69")

if st.button("Calculate BMI"):
    if not weight_input or not height_input:
        st.warning("Please enter both weight and height before calculating BMI.")
    else:
        try:
            weight = float(weight_input)
            height = float(height_input)
        except ValueError:
            st.error("Please enter valid numeric values for weight and height.")
            st.stop()

        if height <= 0 or weight <= 0:
            st.error("Weight and height must be greater than zero.")
        else:
            if unit_system == "Metric (kg, cm)":
                height_m = height / 100
                bmi = weight / (height_m ** 2)
                ideal_low = 18.5 * (height_m ** 2)
                ideal_high = 24.9 * (height_m ** 2)
            else:
                bmi = 703 * weight / (height ** 2)
                ideal_low = 18.5 * (height ** 2) / 703
                ideal_high = 24.9 * (height ** 2) / 703

            bmi = round(bmi, 1)
            ideal_low = round(ideal_low, 1)
            ideal_high = round(ideal_high, 1)

            if bmi < 18.5:
                category = "Underweight"
                advice = "Consider gaining weight through a balanced diet and strength training."
            elif bmi < 25:
                category = "Normal weight"
                advice = "Great job! Maintain your healthy lifestyle."
            elif bmi < 30:
                category = "Overweight"
                advice = "Try regular exercise and a balanced diet to move toward a healthier range."
            else:
                category = "Obesity"
                advice = "Speak with a healthcare professional for personalized guidance."

            st.success(f"Your BMI is {bmi}")
            st.info(f"Category: {category}")
            st.write(f"Ideal weight range for your height: {ideal_low} to {ideal_high} {'kg' if unit_system.startswith('Metric') else 'lb'}")
            st.write(advice)
            st.markdown("\n**BMI categories:** Underweight &lt; 18.5, Normal 18.5–24.9, Overweight 25–29.9, Obesity ≥ 30")
