import streamlit as st
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import pickle

model = pickle.load(open("prediction_pl.pkl","rb"))



st.title("Churn-Prediction Project")

SeniorCitizen = st.number_input("Select SeniorCitizen :",min_value = 0,max_value = 1, key='input1')
tenure = st.number_input("Select tenure:",min_value = 0,max_value = 100, key='input1')
Contract = st.number_input("Select Contract:",min_value = 0,max_value = 1, key='input1')
MonthlyCharges = st.number_input("Select MonthlyCharges:",min_value = 0,max_value = 1000, key='input1')
TotalCharges = st.number_input("Select TotalCharges:",min_value = 0,max_value = 10000, key='input1')
gender_Male = st.number_input("Select gender_Male:",min_value = 0,max_value = 1, key='input1')
Partner_Yes = st.number_input("Select Partner_Yes:",min_value = 0,max_value = 1, key='input1')
Dependents_Yes = st.number_input("Select Dependents_Yes:",min_value = 0,max_value = 1, key='input1')
PhoneService_Yes = st.number_input("Select PhoneService_Yes:",min_value = 0,max_value = 1, key='input1')
OnlineSecurity_Yes = st.number_input("Select OnlineSecurity_Yes:",min_value = 0,max_value = 1, key='input1')
OnlineBackup_Yes = st.number_input("Select OnlineBackup_Yes:",min_value = 0,max_value = 1, key='input1')
DeviceProtection_Yes = st.number_input("Select DeviceProtection_Yes:",min_value = 0,max_value = 1, key='input1')
TechSupport_Yes = st.number_input("Select TechSupport_Yes:",min_value = 0,max_value = 1, key='input1')
StreamingTV_Yes = st.number_input("Select StreamingTV_Yes:",min_value = 0,max_value = 1, key='input1')
StreamingMovies_Yes = st.number_input("Select StreamingMovies_Yes:",min_value = 0,max_value = 1, key='input1')
PaperlessBilling_Yes = st.number_input("Select PaperlessBilling_Yes:",min_value = 0,max_value = 1, key='input1')
PaymentMethod_Credit = st.number_input("Select PaymentMethod_Credit card (automatic):",min_value = 0,max_value = 1, key='input1')
PaymentMethod_Electronic  = st.number_input("Select PaymentMethod_Electronic :",min_value = 0,max_value = 1, key='input1')
PaymentMethod_Mailed  = st.number_input("Select PaymentMethod_Mailed :",min_value = 0,max_value = 1, key='input1')
MultipleLines_No = st.number_input("Select MultipleLines_No:",min_value = 0,max_value = 1, key='input1')
MultipleLines_Yes = st.number_input("Select MultipleLines_Yes:",min_value = 0,max_value = 1, key='input1')
InternetService_Fiber = st.number_input("Select InternetService_Fiber:",min_value = 0,max_value = 1, key='input1')
InternetService_No = st.number_input("Select InternetService_No:",min_value = 0,max_value = 1, key='input1')
 
if st.button("Submit"):
    prediction = model.predict([['SeniorCitizen', 'tenure', 'Contract', 'MonthlyCharges',
       'TotalCharges', 'gender_Male', 'Partner_Yes', 'Dependents_Yes',
       'PhoneService_Yes', 'MultipleLines_No phone service',
       'MultipleLines_Yes', 'InternetService_Fiber optic',
       'InternetService_No', 'OnlineSecurity_Yes', 'OnlineBackup_Yes',
       'DeviceProtection_Yes', 'TechSupport_Yes', 'StreamingTV_Yes',
       'StreamingMovies_Yes', 'PaperlessBilling_Yes',
       'PaymentMethod_Credit card (automatic)',
       'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']])[0]
    st.write("The predicted value is:", prediction)

