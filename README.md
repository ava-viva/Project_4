# Tuberculosis Prediction using Machine Learning
**#Introduction**
In our previous project, we focused on visualizing the worldwide trend of Tuberculosis (TB). Now, we are taking our research a step further with this new project. The primary objective of this project is to detect crucial features from diverse datasets that can be utilized to predict TB occurrence in different countries.
Tuberculosis (TB) is an infectious disease caused by Mycobacterium tuberculosis, primarily affecting the lungs. Its incidence in countries is influenced by various factors. The health system's quality and accessibility play a critical role in early detection, diagnosis, and treatment. Access to clean water and proper sanitation is vital, as poor water quality can increase susceptibility to TB. Climate conditions, such as cold and damp environments, can promote TB transmission, and climate change may exacerbate the issue. Health factors like malnutrition and weakened immune systems due to conditions like HIV/AIDS elevate the risk of TB. Additionally, overcrowded living conditions and poor ventilation facilitate bacterial transmission. Effectively addressing TB requires a comprehensive approach considering medical and social determinants of health.

![Tuberculosis](https://github.com/ava-viva/Project_4/assets/53435881/ce5f7ffe-ac8e-4655-9c9a-1d48b8dfa1a2)


**#Dataset**
For this project, we have used the World Development Indicators dataset available on Kaggle. The dataset contains various indicators by countries, including emissions data. You can access the dataset at the following link: World Development Indicators by Countries.
https://www.kaggle.com/datasets/hn4ever/world-development-indicators-by-countries

**#Preprocessing**
Before performing the feature selection and model building, we applied preprocessing steps to clean the data. We handled missing values (NaNs) by replacing them with the average value of the respective feature.

**#Feature Selection**
To identify the most relevant features that can aid in predicting TB occurrence, we utilized three feature selection methods:
-Chi-square Test (chi-squere): A statistical method to determine the independence of variables.
-Recursive Feature Elimination (RFE): A technique to recursively remove the least significant features until an optimal subset is obtained.
-Correlation Matrix: Analyzing the correlation between features to identify the most influential ones.

**#Model Selection**
To predict TB occurrence, we evaluated the performance of multiple machine learning models:
-Random Forest: An ensemble learning method that builds multiple decision trees and combines their outputs to make predictions.
-Neural Network (NN): A deep learning model inspired by the structure and functioning of the human brain, known for its ability to handle complex data.
-Linear Regression: A basic linear model that fits a line to the data points to make predictions.
-Support Vector Machine (SVM): A supervised learning algorithm used for classification and regression tasks.
-Decision Tree: A tree-like model that breaks down data into smaller subsets based on features.

**#Model Performance**
After evaluating the models, we found that the Neural Network (NN) exhibited the highest accuracy in predicting TB occurrence from the given features.
#Prediction and User Interface
Using the trained Neural Network model, we made predictions on new data. To provide a user-friendly interface for exploring and visualizing the predicted results, we developed an HTML/Flask app. This app allows users to input data and view the predicted outcomes.

**#Conclusion**
With this project, we have taken significant steps towards predicting TB occurrence using machine learning techniques. The combination of data preprocessing, feature selection, and model evaluation has provided us with valuable insights into the contributing factors for TB prevalence in different countries. By employing the Neural Network model and creating a user interface, we aim to make this predictive tool accessible and useful for researchers and policymakers in the field of public health.
