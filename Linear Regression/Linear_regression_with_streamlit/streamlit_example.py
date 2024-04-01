"""
first we need to install streamlit 
do
pip install streamlit

or

install the requirement
do 
pip install -r requirement.txt


in order to run streamlit file

streamlit run <python file name>
for this file

streamlit run streamlit_example.py
"""


import streamlit as st

st.title("Linear Regression Application")
st.text("Hello this first streamlit application")
st.text_input("Full Name", "Enter your name here")
# st.text_area(label="review")
st.button("Submit")
