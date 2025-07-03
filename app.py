import streamlit as st
import pickle
st.title('Insurance Premium Prediction App')
print('Pune')
age=int(st.text_input('Enter your age:'))
gender=st.text_input('Enter gender(male/female):')
gender= 0 if gender=='male' else 1
bmi=float(st.text_input('Enter bmi'))
children=int(st.text_input('Enter no of childrens'))
smoker=st.text_input('Do you smoke(yes/no)')
smoker= 1 if smoker=='yes' else 0
X_test=[[age,gender,bmi,children,smoker]]
# Load the model
model = pickle.load(open('model.pkl', 'rb'))
# Make predictions using the testing data
yp = model.predict(X_test)
st.write('Insurance Premium',yp)