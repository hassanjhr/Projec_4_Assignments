import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    st.title("🧍‍♂️ BMI Calculator 🧍‍♀️")

    st.write("Enter your weight and height to calculate your Body Mass Index (BMI). ⚖️")

    weight = st.number_input("⚖️ Weight (in kilograms)", min_value=1.0, max_value=500.0, step=0.1)
    height = st.number_input("📏 Height (in meters)", min_value=0.5, max_value=3.0, step=0.01)

    if st.button("🧮 Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: **{bmi:.2f}**")

        if bmi < 18.5:
            st.warning("⚠️ You are underweight. 🥗")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a normal weight. 🎉")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are overweight. 🏋️‍♂️")
        else:
            st.error("🚨 You are obese. Please consult a healthcare professional. 🩺")

if __name__ == "__main__":
    main()