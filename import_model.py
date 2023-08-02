from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np
model_path = "path/trained_model.h5"  
model = load_model(model_path)
# Normalize the input data using MinMaxScaler 
scaler_series = MinMaxScaler(feature_range=(0, 1))
scaler_series.fit(X[:, :7])  
input_series_normalized = scaler_series.transform(input_series.reshape(1, -1))

# Make predictions using the loaded model
y_pred_series = model.predict(input_series_normalized)

# The predictions will be in the form of probabilities, so you might want to round them to get class labels (0 or 1)
y_pred_class_series = y_pred_series.round()

# Convert the predicted class label to an integer (0 or 1)
predicted_class = int(y_pred_class_series[0][0])

# Print the predicted class
print("Predicted Class:", predicted_class)