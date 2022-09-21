import pandas as pd
import streamlit as st
import joblib
from PIL import Image

#image3 = Image.open('https://raw.githubusercontent.com/Niklewa/Diabetes_pima_indians/main/to_app/sugar-blood-level.png')
#image4 = Image.open('diabetes.png')
# streamlit run streamlit_fhs.py
# cd C:\Users\nikod\PycharmProjects\scientificProject\to_app

st.write('''<center><p><span style="font-size:38px","font-family:'Times New Roman'">
         <strong>Diabetes Predictor</strong></p></center>''',
		 unsafe_allow_html=True )
'''
col11, col12, col13, col14, col15 = st.columns(5)
with col11:
    st.write("#")
with col13:
    st.image(image4, width=100)
with col12:
     st.write("#")
with col14:
     st.write("#")
with col15:
     st.write("#")
'''
st.write("#")
st.write("#")

col1, col2, col3, col4 = st.columns(4)

Pregnancies = col1.number_input('Pregnancies', min_value=0, max_value=30, step=1)
Glucose = col2.number_input('Glucose level', min_value=0, max_value=1000, step=1)
BloodPressure = col3.number_input('Blood Pressure', min_value=0, max_value=200, step=1)
SkinThickness = col4.number_input('Skin Thickness', min_value=0, max_value=1000, step=1)
Insulin = col1.number_input('Insulin level', min_value=0, max_value=1000, step=1)
BMI = col2.number_input('BMI', min_value=0.0, max_value=70.0, step=0.1)
DiabetesPedigreeFunction = col3.number_input('Diabetes Pedigree Function', min_value=0.000, max_value=5.000, step=0.001)
Age = col4.number_input('Age', min_value=0, max_value=150, step=1)


df_pred = pd.DataFrame([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]],
                       columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

model = joblib.load('https://raw.githubusercontent.com/Niklewa/Diabetes_pima_indians/main/to_app/lr_diab_model.pkl')
prediction = model.predict(df_pred)

st.write("#")
#image1 = Image.open('checked.png')
#image2 = Image.open('alarm.png')

if st.button('Predict'):

    if(prediction[0]==0):
        st.write('''<p><span style="font-size:24px">You most likely do not have diabetes</span></p>
       ''', unsafe_allow_html=True)
     #   st.image(image1, width=100)


    else:
        st.write('<p><span style="font-size:24px">You most likely have diabetes, please consult with a specialist</span></p>', unsafe_allow_html=True)
      #  st.image(image2, width=100)

st.write("#")
st.write("#")

st.write('''<p><span style="font-size:18px">Variables description:</span>
<ul>
<li><span style="font-size:16px"><strong>Pregnancies</strong>: Number of times pregnant</span></li>
<li><span style="font-size:16px"><strong>Glucose level</strong>: Plasma glucose concentration a 2 hours in an oral glucose tolerance test</span></li>
<li><span style="font-size:16px"><strong>Blood Pressure</strong>: Diastolic blood pressure (mm Hg)</span></li>
<li><span style="font-size:16px"><strong>Skin Thickness</strong>: Triceps skin fold thickness (mm)</span></li>
<li><span style="font-size:16px"><strong>Insulin level</strong>: 2-Hour serum insulin (mu U/ml)</span></li>
<li><span style="font-size:16px"><strong>BMI</strong>: Body mass index (weight in kg/(height in m)^2)</span></li>
<li><span style="font-size:16px"><strong>Diabetes Pedigree Function</strong>: Diabetes pedigree function</span></li>
<li><span style="font-size:16px"><strong>Age</strong>: Age (years)</span></li>
</ul></p>''', unsafe_allow_html=True)

# Import model that you are sure is correct
# Work on the look of the app
# Work on the reactivity, make those shitty boxes look better, and lower the number of possible values (add some constraints)
# Move it into a server in order to make it accesible for everyone on the web
