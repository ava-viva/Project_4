
#importing libraries
import tensorflow as tf
import pandas as pd
import numpy as np

# Load the trained model from the .h5 file
model_path = "D:/BC class/project 4/trained_model.h5"  # Update the path to the trained_model.h5 file
loaded_model = tf.keras.models.load_model(model_path)

# Prepare the new data for prediction
new_data = np.array([[0.000000, 1.00000, 0.300000, 0.100000, 0.100000, 0.000000, 0.300000]])  # Replace with your new data
# Make sure the new_data has the same features and preprocessing as the training data

# Perform prediction using the loaded model
y_pred = loaded_model.predict(new_data)

# Since the prediction output will be in the form of probabilities (for binary classification), you might want to round the predictions to get class labels (0 or 1)
y_pred_class = y_pred.round()

print("Predicted probabilities:", y_pred)
print("Predicted class labels:", y_pred_class)















