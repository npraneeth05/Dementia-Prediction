import streamlit as st
import numpy as np
import pandas as pd

from sklearn.preprocessing import  StandardScaler



st.title('Dementia Prediction App 🤖')

st.info('Early diagnosis for better future..🩺🔬')

with st.expander('Data'):
  df = pd.read_csv('https://raw.githubusercontent.com/npraneeth05/Dementia-Prediction/refs/heads/master/dementia_dataset.csv')
  df
  st.write('*X*')
  df = df.drop(["MMSE"],axis=1,inplace=True)
  df = df.drop(["SES"],axis=1)
  df = df.drop(["Subject ID"],axis=1,inplace=True)
  df = df.drop(["MRI ID"],axis=1,inplace=True)
  df = df.drop(["Visit"],axis=1,inplace=True)
  df = df.drop(["Hand"],axis=1,inplace=True)
  df = df.drop(["ASF"],axis=1,inplace=True)
  df["M/F"].replace({"M":0,"F":1},inplace=True)
  df["Group"].replace({"Nondemented":0,"Demented":1,"Converted":0},inplace=True)
  df.fillna(data.mean,inplace=True)
  X_raw= df.drop("Group", axis=1)
  X_raw

  st.write('*y*')
  y_raw = df["Group"]
  y_raw
  
with st.sidebar:
  st.header('Input Features')
  Gender = st.selectbox ('Gender', ('Male', 'Female'))
  Age = st.slider('Age', 0, 100, 45)
  MR_Delay = st.slider('MR-Delay', 0, 3000, 1000)
  EDUC = st.slider('Education', 0, 17, 25)
  CDR = st.selectbox('CDR', (0.0, 0.5, 1.0, 2.0))
  ETIV = st.slider('eTIV', 1000, 1500, 2000)
  NWBW = st.slider('nWBW', 0.0001, 0.681, 1.000)
if st.button("predict"):
    data = {'M/F': Gender,
            'Age': Age,
            'MR Delay': MR_Delay,
            'EDUC': EDUC,
            'CDR': CDR,
            'eTIV': ETIV,
            'nWBV': NWBW}
    
    
    input_df = pd.DataFrame(data, index=[0])
    input_df=input_df["M/F"].replace({"Male":0,"Female":1},inplace=True)
    input_values = pd.concat([input_df, X_raw], axis=0)
    
    
    scaler =StandardScaler()
    input_values = scaler.fit_transform(input_values)
    
    arr = np.array(input_values)
    input =arr[0, :]
    input_values =arr[1:, :]
    
    with st.expander('Input features'):
      st.write('*Input values*')
      input_df
      st.write('*Combined input data*')
      input_values
    

    
    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(input_values, y_raw, test_size=0.2, random_state=42)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


    nb_clf = GaussianNB()


    nb_clf.fit(xtrain, ytrain)

    y = nb_clf.predict(xtest)

    
    # Making predictions
    y = rf_classifier.predict(input)
    if y[0]==0:
      st.warning("demented")
    elif y[0]==1:
      st.success("not demented")
    else:
      st.warning("converted")
