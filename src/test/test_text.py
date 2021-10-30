import sys
import streamlit as st
import pandas as pd

sys.path.append('D:/Assingment/src')
import text 

#name = st.file_uploader("Pick a File")


def get_name_test(col_name,serie):
    dt = text.TextColumn(col_name,serie)
    name = dt.get_name()
    st.header("Field Name : " + str(name))

def get_whitespace_test(col_name,serie):
    dt = text.TextColumn(col_name,serie)
    name = dt.get_whitespace()
    return ["Number of rows with only Whitespaces " , str(name)]

def get_unique_test(col_name,serie):
    dt = text.TextColumn(col_name,serie)
    count = dt.get_unique()
    return ["Number of Unique Values " , str(count)]

def get_missing_test(col_name,serie):
    dt = text.TextColumn(col_name,serie)
    misscount = dt.get_missing()
    return ["Number of Missing Values " , str(misscount)]

def get_empty_test(col_name,serie):
    dt = text.TextColumn(col_name,serie)
    emptcount = dt.get_empty()
    return ["Number of Empty Rows " , str(emptcount)]

def get_lowercase_test(col_name,serie):
    dt = text.TextColumn(col_name,serie)
    lower_case = dt.get_lowercase()
    return ["Number of Rows with only Lowercases " , str(lower_case)]

def get_uppercase_test(col_name,serie):
    dt = text.TextColumn(col_name,serie)
    upper_case = dt.get_uppercase()
    return ["Number of Rows with only Uppercases " , str(upper_case)]

def get_alphabet_test(col_name,serie):
    dt = text.TextColumn(col_name,serie)
    alpha = dt.get_alphabet()
    return ["Number of Rows with only Alphabets " , str(alpha)]

def get_digit_test(col_name,serie):
    dt = text.TextColumn(col_name,serie)
    numerics = dt.get_digit()
    return ["Number of Rows with only digits " , str(numerics)]

def get_mode_test(col_name,serie):
    dt = text.TextColumn(col_name,serie)
    mode = dt.get_mode()
    return ["Mode Value " , str(mode)]

def get_frequent_test(col_name,serie):
    st.subheader("Most Frequent Values: ")
    dt = text.TextColumn(col_name,serie)
    freq_val = dt.get_frequent()
    st.dataframe(freq_val)

def get_barchart_test(col_name,serie):
    st.subheader("Bar Chart ")
    dt = text.TextColumn(col_name,serie)
    freq = dt.get_barchart()
    st.bar_chart(freq)
