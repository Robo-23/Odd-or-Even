import streamlit as st

st.write("""
# Odd or Even
This app tells if the number is Odd or Even
""")
#Get Input

st.header('User Input Parameters')
number = float(st.number_input("GIVEN_NUMBER"))

if number % 2==0:
    st.subheader('Number is Even')
else:
    st.subheader('Number is Odd')


