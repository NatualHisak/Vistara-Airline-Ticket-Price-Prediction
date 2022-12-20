import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np
import joblib
import json

#Load files
with open('best.pkl', 'rb') as file_1:
  best = joblib.load(file_1)

def run() :
    #membuat form
    with st.form(key='form_parameters'):
        departure = st.selectbox('source_city', ('Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'),index = 0)
        destination = st.selectbox('destination_city', ('Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai', 'Delhi'),index = 0)
        arrival = st.selectbox('arrival_time', ('Afternoon', 'Morning', 'Evening', 'Night', 'Early_Morning', 'Late_Night'),index = 0)
        departuretime = st.selectbox('departure_time', ('Afternoon', 'Morning', 'Evening', 'Night', 'Early_Morning', 'Late_Night'),index = 0)
        type = st.selectbox('class', ('Economy', 'Business'),index = 0)
        st.markdown('---')


        transit = st.selectbox('stops', ('zero', 'one', 'two_or_more'),index = 0)
        durations = st.slider('duration',0.0,50.0, 0.1)
        st.markdown('---')

        days_before = st.number_input('days_left', min_value = 1, max_value = 49, value = 3)
        st.markdown('---')
        
        submitted = st.form_submit_button('Predict!')

    data_inf={
        'source_city' : departure,
        'destination_city' : destination,
        'arrival_time': arrival,
        'departure_time': departuretime,
        'class' : type,
        'stops': transit,
        'duration': durations,
        'days_left' : days_before,
    }

    # Split between Numerical Columns and Categorical Columns
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:


        y_pred_inf = best.predict(data_inf)

        st.write('# Predicted price :', str(int(y_pred_inf)))
        image = Image.open('Vistara.jpg')
        st.image(image,caption = 'Enjoy Vistara Airline!')
if __name__ == '__main__':
    run()