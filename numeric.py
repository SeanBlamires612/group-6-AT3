# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd

pip install altair
import altair as alt


@dataclass
class NumericColumn:
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
    return self.serie.nunique()

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return self.serie.isna().sum()

  def get_zeros(self):
    """
    Return number of occurrence of 0 value for selected column
    """
    return self.(serie == 0).sum()

  def get_negatives(self):
    """
    Return number of negative values for selected column
    """
    return self.(serie ['funded_amnt_inv'] <0).any()

  def get_mean(self):
    """
    Return the average value for selected column
    """
    return self.serie[['funded_amnt']].mean()

  def get_std(self):
    """
    Return the standard deviation value for selected column
    """
    return self.serie[['funded_amnt']].std()
  
  def get_min(self):
    """
    Return the minimum value for selected column
    """
    return self.serie[['funded_amnt', 'funded_amnt_inv', 'int_rate',
       'installment', 'annual_inc', 'dti', 'delinq_2yrs', 'fico_range_low',
       'fico_range_high', 'inq_last_6mths']].min()

  def get_max(self):
    """
    Return the maximum value for selected column
    """
    return self.serie[['funded_amnt', 'funded_amnt_inv', 'int_rate',
       'installment', 'annual_inc', 'dti', 'delinq_2yrs', 'fico_range_low',
       'fico_range_high', 'inq_last_6mths']].max()

  def get_median(self):
    """
    Return the median value for selected column
    """
    return self.serie[['funded_amnt', 'funded_amnt_inv', 'int_rate',
       'installment', 'annual_inc', 'dti', 'delinq_2yrs', 'fico_range_low',
       'fico_range_high', 'inq_last_6mths']].median()

  def get_histogram(self):
    """
    Return the generated histogram for selected column
    """
    alt.data_transformers.disable_max_rows()
    return self.alt.Chart(serie).mark_bar().encode(
    x = alt.X('id', bin=alt.Bin(maxbins=50)),
    y = 'funded_amnt'
)

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    return self.serie[['funded_amnt', 'funded_amnt_inv', 'int_rate',
       'installment', 'annual_inc', 'dti', 'delinq_2yrs', 'fico_range_low',
       'fico_range_high', 'inq_last_6mths']].count()
