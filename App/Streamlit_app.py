from data import Dataset
import streamlit as st
import pandas as pd


st.title('Data Explorer Tool')
file = st.file_uploader("Upload file", type=['csv'])

if not file:
    st.write('Please upload a CSV file to begin')
else:
    df = pd.read_csv(file)
    dataset = Dataset(name=file.name, df=df)
    
    st.subheader('Overall Information')
    st.write(f'**Name of Table:** {dataset.get_name()}')
    st.write(f'**Number of Rows:** {dataset.get_n_rows()}')
    st.write(f'**Number of Columns:** {dataset.get_n_cols()}')
    st.write(f'**Number of Duplicated Rows:** {dataset.get_n_duplicates()}')
    st.write(f'**Number of Rows with Missing Values:** {dataset.get_n_missing()}')
    st.write(f'**List of Columns:** {dataset.get_cols_list()}')
    st.write(f'**Type of Columns:**')
    st.table(dataset.get_cols_dtype().astype(str))
    filter_rows = st.slider('Select the number of rows to be displayed', 1, 50, 5)
    st.write(f'**Top Rows of Table**')
    st.dataframe(dataset.get_head(n=filter_rows))
    st.write(f'**Bottom Rows of Table**')
    st.dataframe(dataset.get_tail(n=filter_rows))
    st.write(f'**Random Sample Rows of Table**')
    st.dataframe(dataset.get_sample(n=filter_rows))
    convert_date = st.multiselect('Which columns do you want to convert to dates', dataset.get_text_columns())
    for column in convert_date:
        dataset.df[column] = pd.to_datetime(dataset.df[column])
