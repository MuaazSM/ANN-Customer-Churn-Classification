import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pickle
import streamlit as st

# Loading the trained model
model = tf.keras.models.load_model('model.h5')

#load the encoders and scalers
with open('onehot_encoder_geo.pkl', 'rb') as file:
    label_encoder_geo = pickle.load(file)

with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


# Streamlit app
st.title("Customer Churn Prediction")

# User Input 
geography = st.selectbox('Geography', label_encoder_geo.categories_[0])
gender = st.selectbox('Gender', ['Female', 'Male'])
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0,1])
is_active_member = st.selectbox('Is Active Member', [0,1])

##mapping gender
gender_mapping = {'Female': 0, 'Male': 1}
gender_value = gender_mapping[gender]

#Prepping the input data
input_data  =pd.DataFrame({
    'CreditScore' : [credit_score],
    'Gender' : [gender_value],
    'Age': [age],
    'Tenure' : [tenure],
    'Balance': [balance],
    'NumOfProducts' : [num_of_products],
    'HasCrCard' : [has_cr_card],
    'IsActiveMember' : [is_active_member],
    'EstimatedSalary' : [estimated_salary]
})

# One hot encoding geo
geo_encoded = label_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns = label_encoder_geo.get_feature_names_out(['Geography']))
#Combining the one hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop = True), geo_encoded_df], axis = 1)
# Scale the input data
input_data_scaled = scaler.transform(input_data)

#Predict Churn
prediction = model.predict(input_data_scaled)
prediction_probablity = prediction[0][0]

st.write(f'Churn Probablity: {prediction_probablity:.2f}')

if prediction_probablity > 0.5:
    st.write("Customer is likely to Churn")
else:
    st.write("Customer is not likely to Churn")