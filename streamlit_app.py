# import streamlit as st
# import numpy as np
# import pandas as pd

# from sklearn.preprocessing import  StandardScaler



# st.title('Dementia Prediction App 🤖')

# st.info('Early diagnosis for better future..🩺🔬')

# with st.expander('Data'):
#   df = pd.read_csv('dementia_dataset.csv')
#   df
#   st.write('*X*')
#   df = df.drop(["MMSE"],axis=1)
#   df = df.drop(["SES"],axis=1)
#   df = df.drop(["Subject ID"],axis=1)
#   df = df.drop(["MRI ID"],axis=1)
#   df = df.drop(["Visit"],axis=1)
#   df = df.drop(["Hand"],axis=1)
#   df = df.drop(["ASF"],axis=1)
#   df["M/F"].replace({"M":0,"F":1},inplace=True)
#   df["Group"].replace({"Nondemented":0,"Demented":1,"Converted":2},inplace=True)
#   df.fillna(df.mean,inplace=True)
#   X_raw= df.drop("Group", axis=1)
#   X_raw

#   st.write('*y*')
#   y_raw = df["Group"]
#   y_raw
  
# with st.sidebar:
#   st.header('Input Features')
#   Gender = st.selectbox ('Gender', ('Male', 'Female'))
#   Age = st.slider('Age', 0, 100, 45)
#   MR_Delay = st.number_input("MR-Delay", min_value=0, max_value=3000, step=1)
#   EDUC = st.slider('Education', 0, 25, 11)
#   CDR = st.selectbox('CDR', (0.0, 0.5, 1.0, 2.0))
#   ETIV = st.number_input("eTIV", min_value=0, max_value=2000, step=1)
#   NWBW = st.slider('nWBW', 0.0001, 1.000, 0.681)
# if st.button("predict"):
#     data = {'M/F': Gender,
#             'Age': Age,
#             'MR Delay': MR_Delay,
#             'EDUC': EDUC,
#             'CDR': CDR,
#             'eTIV': ETIV,
#             'nWBV': NWBW}
    
    
#     input_df = pd.DataFrame(data, index=[0])
#     input_df["M/F"].replace({"Male":0,"Female":1},inplace=True)
#     input_values = pd.concat([input_df, X_raw], axis=0)

    
#     scaler =StandardScaler()
#     input_values = scaler.fit_transform(input_values)
    
#     arr = np.array(input_values)
#     input =arr[0, :]
#     input = input.reshape(1, -1)
#     input_values =arr[1:, :]
#     with st.expander('Input features'):
#       st.write('*Input values*')
#       input_df
#       st.write('*Combined input data*')
#       input_values
    
#     # Splitting the data into training and testing sets
#     from sklearn.model_selection import train_test_split
#     X_train, X_test, y_train, y_test = train_test_split(input_values, y_raw, test_size=0.2, random_state=42)
#     from sklearn.naive_bayes import GaussianNB
   

#     nb_clf = GaussianNB()


#     nb_clf.fit(X_train, y_train)

#     y = nb_clf.predict(input)

#     if y[0]==0:
#       st.success("Your health check-up is clear of disease markers.😄")
#     elif y[0]==1:
#       st.warning("You’ve been diagnosed with Dementia")
#     else:
#       st.warning(" You're in early phrase, proper treatment can control your health condition")


import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

st.set_page_config(page_title="Dementia Prediction System", page_icon="🩺", layout="centered")

st.title('Dementia Prediction System')
st.info('Early diagnosis for a better future.')

with st.expander('Data Overview & Processing'):
    df = pd.read_csv('dementia_dataset.csv')
    st.dataframe(df, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('**Feature Set (X)**')
        df = df.drop(["MMSE", "SES", "Subject ID", "MRI ID", "Visit", "Hand", "ASF"], axis=1)
        df["M/F"].replace({"M": 0, "F": 1}, inplace=True)
        df["Group"].replace({"Nondemented": 0, "Demented": 1, "Converted": 2}, inplace=True)
        df.fillna(df.mean(numeric_only=True), inplace=True)
        X_raw = df.drop("Group", axis=1)
        st.dataframe(X_raw, use_container_width=True)

    with col2:
        st.markdown('**Target Variable (y)**')
        y_raw = df["Group"]
        st.dataframe(y_raw, use_container_width=True)

st.markdown("---")
st.subheader('Patient Clinical Parameters')

col_a, col_b = st.columns(2)

with col_a:
    Gender = st.selectbox('Gender', ('Male', 'Female'))
    Age = st.slider('Age', 0, 100, 45)
    MR_Delay = st.number_input("Gaps between MRI scans", min_value=0, max_value=3000, step=1)
    EDUC = st.slider('Education (Years)', 0, 25, 11)

with col_b:
    CDR = st.selectbox('Clinical Dementia Rating (CDR)', (0.0, 0.5, 1.0, 2.0))
    ETIV = st.number_input("Estimated Total Intracranial Volume", min_value=0, max_value=2000, step=1)
    NWBW = st.slider('Normalized Whole Brain Volume', 0.0001, 1.000, 0.681)

st.markdown("<br>", unsafe_allow_html=True)

btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
with btn_col2:
    predict_button = st.button("Generate Prediction", use_container_width=True, type="primary")

if predict_button:
    data = {'M/F': Gender,
            'Age': Age,
            'MR Delay': MR_Delay,
            'EDUC': EDUC,
            'CDR': CDR,
            'eTIV': ETIV,
            'nWBV': NWBW}
    
    input_df = pd.DataFrame(data, index=[0])
    input_df["M/F"].replace({"Male": 0, "Female": 1}, inplace=True)
    input_values = pd.concat([input_df, X_raw], axis=0)

    scaler = StandardScaler()
    input_values = scaler.fit_transform(input_values)
    
    arr = np.array(input_values)
    user_input = arr[0, :].reshape(1, -1)
    input_values = arr[1:, :]
    
    with st.expander('View Processed Input Data'):
        st.markdown('**Input values**')
        st.dataframe(input_df, use_container_width=True)
    
    X_train, X_test, y_train, y_test = train_test_split(input_values, y_raw, test_size=0.2, random_state=42)
    
    nb_clf = GaussianNB()
    nb_clf.fit(X_train, y_train)

    y = nb_clf.predict(user_input)

    st.markdown("---")
    st.subheader("Diagnostic Prediction")
    
    if y[0] == 0:
        st.success("Result: No dementia markers detected. The health check-up is clear.")
    elif y[0] == 1:
        st.error("Result: Diagnosis indicates Dementia markers.")
    else:
        st.warning("Result: Early phase indicators detected. Proper treatment and monitoring are recommended.")
