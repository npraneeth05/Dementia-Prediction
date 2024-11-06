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
  Gender = st.selectbox ('Gender', ('Male', 'Female'))
  Age = st.slider('Age', 0, 100, 45)
  EDUC = st.slider('Education', 0, 17, 25)
  MMSE = st.slider('MMSE', 5, 17, 30)
  CDR = st.text('CDR', 0.1, 6, 2)
  ETIV = st.slider('eTIV', 1000, 1500, 2000)
  NWBW = st.slider('nWBW', 0.0001, 0.681, 1)
