import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
st.header('Vehicle Data Dashboard')

histogram = px.histogram(df,x='model_year',title ='model year of car')
st.plotly_chart(histogram)


scatter = px.scatter(df,x='model_year',y='condition', title ='model_year vs. condition')
st.plotly_chart(scatter)

if st.checkbox("Show Dataset"):
    st.write(df.head())

    instances = df['condition'].unique().tolist()
    filter = st.selectbox('Filter Cars by Condition',instances)
    new_df = df[df['condition']== filter]
    st.dataframe(new_df)
