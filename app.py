import pandas as pd
import streamlit as st
import plotly.express as px

#Reading Dataset
df = pd.read_csv('vehicles_us.csv')

#Displaying Header for our App
st.header('Vehicle Data Dashboard')

#Adding Histogram to our App
histogram = px.histogram(df,x='model_year',title ='model year of car')
st.plotly_chart(histogram)

#Adding a Scatter Plot to our App
scatter = px.scatter(df,x='model_year',y='condition', title ='model_year vs. condition')
st.plotly_chart(scatter)

#Adding a Checkbox to our App
if st.checkbox("View Dataset with Filter"):

    #Choosing only unique values from condition attribute
    instances = df['condition'].unique().tolist()

    #Filtering out our dataset
    filter = st.selectbox('Filter Cars by Condition',instances)
    new_df = df[df['condition']== filter]

    #Adding Filtered Dataset to our app
    st.write(new_df)
