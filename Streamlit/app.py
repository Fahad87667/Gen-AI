import streamlit as st
import pandas as pd
import csv

st.title("Introduction")

name = st.text_input("Enter Your Name")
st.write(f"Your Name is : {name}")

age = st.slider("Enter your age",0,100,0)
st.write(f"Your age is : {age}")

options = "Python", "Java", 'C++', 'C'

choice = st.selectbox('Select Your Favorite Programming language ',options)
st.write(f'You selected : {choice}')

# Create a dictionary with known data
data = {
    'Name': [
        'Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince',
        'Edward Elric', 'Fiona Green', 'George Lucas', 'Hannah Baker',
        'Ian Wright', 'Julia Roberts'
    ],
    'Age': [29, 34, 22, 31, 27, 45, 38, 26, 33, 41],
    'City': [
        'New York', 'Los Angeles', 'Chicago', 'Houston',
        'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego',
        'Dallas', 'San Jose'
    ],
    'Salary': [55000, 72000, 48000, 62000, 50000, 80000, 90000, 53000, 60000, 75000],
    'Department': [
        'Marketing', 'IT', 'Finance', 'HR',
        'Engineering', 'Sales', 'Management', 'IT',
        'Finance', 'Marketing'
    ]
}
 
df = pd.DataFrame(data)
df.to_csv("Sample.csv")

uploader_button = st.file_uploader("Choose a csv file",type="csv")

if uploader_button is not None:
    df = pd.read_csv(uploader_button)
    st.write(df)