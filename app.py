from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model("/Users/ranamousavi/Desktop/Project 4/trained_model.h5")

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    FuelAccess = float(request.form['Fuel Access'])
    Renewableenergyconsumption = float(request.form['Renewable energy consumption'])
    Agriculturalemployment = float(request.form['Agricultural employment'])
    healthexpenditure = float(request.form['Health expenditure'])
    HealthworkersPhysicians = float(request.form['Health workers Physicians'])
    impactPopulation = float(request.form['Impact Population'])
    Ruralpopulation = float(request.form['Rural population'])

    # Create the feature vector for the model prediction
    features = [FuelAccess, Renewableenergyconsumption, Agriculturalemployment, healthexpenditure, HealthworkersPhysicians, impactPopulation, Ruralpopulation]

    # Make the prediction using the loaded model
    features_array = np.array([features])  # Convert to a 2D numpy array
    prediction_probability = model.predict(features_array)[0][0]
    risk_level = "Your country is at high risk for Tuberculosis, and needs to strengthen screening, improve healthcare access, and raise public " if prediction_probability >= 0.5 else " Your country is at low risk for Tuberculosis, and needs to enhance prevention measures, implement infection control, and encourage regular screenings. "

    prediction = f" {risk_level}."

    return render_template('index.html', result=prediction)

if __name__ == "__main__":
    app.run(debug=True)
