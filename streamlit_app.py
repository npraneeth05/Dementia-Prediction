import streamlit as st
import pandas as pd

st.title('Dementia Prediction App 🤖')

st.info('Early diagnosis for better future..🩺🔬')

with st.expander('Data'):
  df = pd.read_csv('')

  
with st.sidebar:
  st.header('Input Features')
  #Age,EDUC,MMSE,CDR,eTIV,nWBV
  Gender = st.selectbox('Gender', ('Male', 'Female'))
  
