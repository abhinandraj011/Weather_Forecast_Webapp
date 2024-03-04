import streamlit as st
import plotly.express as px



st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days= st.slider("Forecast Days",max_value=5,min_value=1,help="Select the number of Forecasted Days")
option =st.selectbox("Select Date to view",options=("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

figure = px.line(x,y, labels)
st.plotly_chart()

