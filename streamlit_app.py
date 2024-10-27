import streamlit as st
import pandas as pd

st.title('Dementia Prediction App 🤖')

st.info('Early diagnosis for better future..🩺🔬')

df = pd.read_csv('https://raw.githubusercontent.com/npraneeth05/Dementia-Prediction/refs/heads/master/dementia_dataset.csv')
