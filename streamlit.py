import streamlit as st
import os
from typing import Dict

from dotenv import load_dotenv

load_dotenv(".env")

from model_call import azure_model_rest_api_call

## Defining the environment variables
API_KEY = os.environ["model_api_key"]


class StreamlitApp:
    def __init__(self):
        # Initialize any variables or configurations
        self.title = "Input to get the model predictions"
        self.age = 25
        self.blood_pressure = 65
        self.bmi = 22
        self.diabetes_pedigree_function = 0.2
        self.glucose = 85
        self.insulin = 60
        self.pregnancies = 1
        self.skin_thickness = 1

    def format_data_for_the_api_call(
        age: float,
        blood_pressure: float,
        bmi: float,
        diabetes_pedigree_function: float,
        glucose: float,
        insulin: float,
        pregnancies: int,
        skin_thickness: int,
    ) -> Dict:

        request_body = {
            "data": [
                {
                    "age": age,
                    "blood_pressure": blood_pressure,
                    "bmi": bmi,
                    "diabetes_pedigree_function": diabetes_pedigree_function,
                    "glucose": glucose,
                    "insulin": insulin,
                    "pregnancies": pregnancies,
                    "skin_thickness": skin_thickness,
                }
            ]
        }

        return request_body

    def render_take_input(self):
        # Main method to render the Streamlit app
        st.title(self.title)

        # Get user inputs
        input_age = st.number_input("Enter the age of the patient:", value=self.age)
        input_blood_pressure = st.slider(
            "Enter blood pressure:",
            min_value=0,
            max_value=100,
            value=self.blood_pressure,
        )
        input_bmi = st.slider("Enter BMI:", min_value=15, max_value=25, value=self.bmi)
        input_diabetes_pedigree_function = st.slider(
            "Enter the diabetes pedigree function:",
            min_value=0.05,
            max_value=2.5,
            value=self.diabetes_pedigree_function,
        )
        input_glucose = st.slider(
            "Enter the glucose:", min_value=60, max_value=100, value=self.glucose
        )
        input_insulin = st.number_input("Enter the insulin:", value=self.insulin)
        input_pregnancies = st.number_input(
            "Enter the number of pregnancies:", value=self.pregnancies
        )
        input_skin_thickness = st.number_input(
            "Enter the skin thickness:", value=self.skin_thickness
        )

        formatted_data = StreamlitApp.format_data_for_the_api_call(
            input_age,
            input_blood_pressure,
            input_bmi,
            input_diabetes_pedigree_function,
            input_glucose,
            input_insulin,
            input_pregnancies,
            input_skin_thickness,
        )

        return formatted_data

    def call_function(self, api_key, formatted_data):

        # Display the submitted input
        if st.button("Submit"):
            model_output = azure_model_rest_api_call(api_key, formatted_data)
            # st.write(model_output)
            model_op_class_pred = model_output[0]
            if model_op_class_pred == 1:
                st.write("Diabetic")
            else:
                st.write("Not Diabetic")


# Create an instance of the app and run it
if __name__ == "__main__":
    print("Quacks like a duck and runs like a goose")
    app = StreamlitApp()
    formatted_data = app.render_take_input()
    app.call_function(API_KEY, formatted_data)
