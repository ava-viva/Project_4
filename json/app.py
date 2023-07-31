# app.py

from flask import Flask, render_template, request
import pickle
import json
from tensorflow.keras.models import load_model
import os

MODEL_PATH = os.path.join("static", "trained_model.h5")

app = Flask(__name__)

# # Load the ML model
# with open('health_fctor_prediction.ipynb', 'rb') as model_file:
#     model = pickle.load(model_file)
trained_model = load_model(MODEL_PATH)

# Load the questionnaire from JSON file
with open('questionnaire.json', 'r') as questions_file:
    questions_data = json.load(questions_file)
    questions = questions_data['questions']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data from the questionnaire
        answers = [request.form.get(f'question_{i}') for i in range(len(questions))]
        print(answers)
        # Prepare the input data for the ML model (convert to numerical format)
        # ... (You'll need to implement this step based on the ML model requirements)

        # Make predictions using the ML model
        prediction = trained_model.predict([answers])[0]
        print(prediction)
        # Map prediction to result
        predicted_result = "Positive" if prediction == 1 else "Negative"

        # Render the result page with the prediction
        return render_template('result.html', prediction=predicted_result)

    # Render the questionnaire page for GET request
    return render_template('questionnaire.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
