import streamlit as st
import pandas as pd

st.title('Dementia Prediction App 🤖')

st.info('Early diagnosis for better future..🩺🔬')

with st.expander('Data'):
  df = pd.read_csv('https://raw.githubusercontent.com/npraneeth05/Dementia-Prediction/refs/heads/master/dementia_dataset.csv')
  df

  
with st.sidebar:
  st.header('Input Features')
  #Age,EDUC,MMSE,CDR,eTIV,nWBV
  Gender = st.selectbox ('Gender', ('Male', 'Female'), 'color'=cyan)
  Age = st.slider('Age', 0, 45, 100)
  EDUC = st.slider('Education', 0, 17, 25)
  
  
