import streamlit as st

st.write("""
# Odd or Even
This app tells if the number is Odd or Even
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    number = st.number_input("GIVEN_NUMBER",min_value=0,max_value=100,step=1)
    return number

if number % 2==0:
    st.write('Number is Even')
else:
    st.write('Number is Odd')


