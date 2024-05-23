from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('heart_disease_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    form_data = request.form

    # Initialize a dictionary with all values as 0
    data = {
        'Smoking': 0, 'AlcoholDrinking': 0, 'Stroke': 0, 'DiffWalking': 0, 'Sex': 0,
        'Diabetic': 0, 'PhysicalActivity': 0, 'Asthma': 0, 'KidneyDisease': 0, 'SkinCancer': 0,
        'AgeCategory_18-24': 0, 'AgeCategory_25-29': 0, 'AgeCategory_30-34': 0,
        'AgeCategory_35-39': 0, 'AgeCategory_40-44': 0, 'AgeCategory_45-49': 0,
        'AgeCategory_50-54': 0, 'AgeCategory_55-59': 0, 'AgeCategory_60-64': 0,
        'AgeCategory_65-69': 0, 'AgeCategory_70-74': 0, 'AgeCategory_75-79': 0,
        'AgeCategory_80 or older': 0, 'GenHealth_Excellent': 0, 'GenHealth_Fair': 0,
        'GenHealth_Good': 0, 'GenHealth_Poor': 0, 'GenHealth_Very good': 0,
        'Race_American Indian/Alaskan Native': 0, 'Race_Asian': 0, 'Race_Black': 0,
        'Race_Hispanic': 0, 'Race_Other': 0, 'Race_White': 0, 'BMI': 0, 'PhysicalHealth': 0,
        'MentalHealth': 0, 'SleepTime': 0
    }

    # Update the values based on form data
    for key in data.keys():
        if key in form_data:
            data[key] = 1

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data, index=[0])

    # Use the DataFrame in the prediction model
    prediction = model.predict(df)

    output = 'Heart Disease Detected' if prediction[0] == 1 else 'No Heart Disease Detected'

    return render_template('index.html', prediction_text='Prediction: {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
