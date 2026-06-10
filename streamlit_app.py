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

st.set_page_config(
    page_title="Dementia Prediction",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>

.main-title{
    text-align:center;
    color:#1E3A8A;
    font-size:42px;
    font-weight:700;
    margin-bottom:5px;
}

.sub-title{
    text-align:center;
    color:#6B7280;
    font-size:18px;
    margin-bottom:30px;
}

div[data-testid="stForm"]{
    background-color:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

.stButton > button{
    width:100%;
    background-color:#2563EB;
    color:white;
    font-weight:bold;
    border-radius:10px;
    height:3em;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<p class="main-title">Dementia Prediction App 🤖</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Early Diagnosis for Better Future 🩺🔬</p>',
    unsafe_allow_html=True
)

df = pd.read_csv("dementia_dataset.csv")

df = df.drop(["MMSE"], axis=1)
df = df.drop(["SES"], axis=1)
df = df.drop(["Subject ID"], axis=1)
df = df.drop(["MRI ID"], axis=1)
df = df.drop(["Visit"], axis=1)
df = df.drop(["Hand"], axis=1)
df = df.drop(["ASF"], axis=1)

df["M/F"].replace({"M": 0, "F": 1}, inplace=True)
df["Group"].replace(
    {
        "Nondemented": 0,
        "Demented": 1,
        "Converted": 2
    },
    inplace=True
)

df.fillna(df.mean(), inplace=True)

X_raw = df.drop("Group", axis=1)
y_raw = df["Group"]

left, center, right = st.columns([1, 2, 1])

with center:

    with st.form("prediction_form"):

        st.subheader("Patient Information")

        Gender = st.selectbox(
            "Gender",
            ("Male", "Female")
        )

        Age = st.slider(
            "Age",
            0,
            100,
            45
        )

        MR_Delay = st.number_input(
            "MR Delay",
            min_value=0,
            max_value=3000,
            step=1
        )

        EDUC = st.slider(
            "Education",
            0,
            25,
            11
        )

        CDR = st.selectbox(
            "CDR",
            (0.0, 0.5, 1.0, 2.0)
        )

        ETIV = st.number_input(
            "eTIV",
            min_value=0,
            max_value=2000,
            step=1
        )

        NWBW = st.slider(
            "nWBV",
            min_value=0.0001,
            max_value=1.0000,
            value=0.6810
        )

        predict_btn = st.form_submit_button(
            "Predict Dementia Risk"
        )

if predict_btn:

    data = {
        'M/F': Gender,
        'Age': Age,
        'MR Delay': MR_Delay,
        'EDUC': EDUC,
        'CDR': CDR,
        'eTIV': ETIV,
        'nWBV': NWBW
    }

    input_df = pd.DataFrame(data, index=[0])

    input_df["M/F"].replace(
        {
            "Male": 0,
            "Female": 1
        },
        inplace=True
    )

    input_values = pd.concat([input_df, X_raw], axis=0)

    scaler = StandardScaler()
    input_values = scaler.fit_transform(input_values)

    arr = np.array(input_values)

    input_data = arr[0, :]
    input_data = input_data.reshape(1, -1)

    input_values = arr[1:, :]

    X_train, X_test, y_train, y_test = train_test_split(
        input_values,
        y_raw,
        test_size=0.2,
        random_state=42
    )

    nb_clf = GaussianNB()

    nb_clf.fit(X_train, y_train)

    y = nb_clf.predict(input_data)

    st.subheader("Prediction Result")

    if y[0] == 0:
        st.success("✅ Your health check-up is clear of disease markers.")

    elif y[0] == 1:
        st.error("⚠️ You have been classified in the Demented category.")

    else:
        st.warning("🟡 You are classified in the Converted category. Early treatment and regular monitoring are recommended.")
