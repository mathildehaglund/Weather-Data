import pandas as pd
import streamlit as st

data = pd.read_csv("Weather_Data.csv", index_col=0)

st.write("""# Weather Data """)

data

temperature = data["Temperature (C)"].head(n=10)
apparent_temperature = data["Apparent Temperature (C)"].head(n=10)

st.write(" Temperature Data ")
temperature

st.write(" Apparent Temperature Data ")
apparent_temperature

st.line_chart(temperature)

st.line_chart(apparent_temperature)

st.write( "Combined plot ")
st.line_chart(data.head(n=10))