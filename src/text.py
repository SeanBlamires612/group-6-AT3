import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class TextColumn:
  col_name: str
  serie: pd.Series
  
  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    unique = self.serie.nunique()
    return unique

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    missing_na = self.serie.isna().sum()
    return missing_na

  def get_empty(self):
    """
    Return number of rows with empty string for selected column
    """
    empty_rows = (self.serie.values == '').sum()  
    return empty_rows

  def get_whitespace(self):
    """
    Return number of rows with only whitespaces for selected column
    """
    whitespace = self.serie.str.fullmatch(r"\s*").sum()
    return whitespace

  def get_lowercase(self):
    """
    Return number of rows with only lower case characters for selected column
    """
    lower = self.serie.str.contains(r'[a-z]')
    lower = lower.to_frame()
    return lower[self.col_name].values.sum()

  def get_uppercase(self):
    """
    Return number of rows with only upper case characters for selected column
    """
    upper = self.serie.str.contains(r'[A-Z]')
    upper = upper.to_frame()
    return upper[self.col_name].values.sum()
  
  def get_alphabet(self):
    """
    Return number of rows with only alphabet characters for selected column
    """
    alpha_cols = self.serie.str.isalpha()
    alpha_cols = alpha_cols.to_frame()
    return alpha_cols[self.col_name].values.sum()

  def get_digit(self):
    """
    Return number of rows with only numbers as characters for selected column
    """
    numeric_cols = self.serie.str.isnumeric()
    numeric_cols = numeric_cols.to_frame()
    return numeric_cols[self.col_name].values.sum()

  def get_mode(self):
    """
    Return the mode value for selected column
    """
    mode_val = self.serie.mode()
    #print(mode_val[0])
    return mode_val[0]

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    freq = self.serie.value_counts().nlargest()
    return freq

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    freq_val = self.serie.value_counts().nlargest(n=20)
    freq_val1 = self.serie.value_counts(normalize=True).nlargest(n=20) * 100
    freq_val = pd.DataFrame({'Value':freq_val.index, 'Occurance':freq_val.values, 'Percentage':freq_val1.values})
    return freq_val
