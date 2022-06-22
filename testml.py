from msilib.schema import Property
import streamlit as st
import pandas as pd
import numpy as np
import pickle


app_mode = st.sidebar.selectbox('Select Page',['Home','Loan Predict'])

if app_mode=='Home': 
    st.title('Loan Status Prediction') 
    st.markdown('Dataset :') 
    df=pd.read_csv('LoanData.csv')
    st.write(df.head()) 
    
# if app_mode=='Home': ## if someone selects the Home Tab
#     st.title('Loan Status Prediction') ##Display text in title formatting
#     st.markdown('Dataset :') ## Display string formatted as Markdown.
#     st.write(df.head()) #write and display out dataset using the command df.head


elif app_mode == 'Loan Predict': # specify our inputs
    st.subheader('Fill in Application details to get prediction ')
    st.sidebar.header("Gender")
    prop = {'Male': "Male", 'Female':"Female"}
    Dependents_s = st.number_input("Dependents", min_value=0, max_value=4)
    Married_s=st.selectbox("Marriage Status",['Married','Unmarried'])
    Education_s=st.selectbox("Educational Status",['Graduated','Not Graduated'])
    Selfemp_s=st.selectbox("Self Employed",['Yes','No'])
    Applicant_Income = st.number_input("Applocant Income")
    Coapplicant_Income = st.number_input("Co-Applicant Income")
    Loanamt=st.number_input("Loan Amount")
    LoanTerm=st.number_input('Loan Repayment Term',min_value=0)
    Credit_history=st.number_input("Credit History",min_value=0.0,max_value=1.0)
    Property_s=st.selectbox("Property Area",['Urban','Semiurban','Rural'])
    Gender_S = st.sidebar.radio("Select Gender ",tuple(prop.keys()))

    Gender=0
    
    if Gender_S == 'Male':
        Gender=1
    elif Gender_S == 'Female':
        Gender=0
        
    if Married_s=='Married':
        Married=1
    elif Married_s=='Unmarried':
        Married=0

    if Dependents_s>0:
        Dependents=1
    else:
        Dependents=0
    
    if Education_s=='Graduated':
        Education=1
    elif Education_s=='Ungraduated':
        Education=0
        
    if Selfemp_s=='Yes':
        Selfemp=1
    elif Selfemp_s=='No':
        Selfemp=0
        
    if Property_s=='Urban' or Property_s=='Semiurban':
        Property_Area=1
    elif Property_s=='Rural':
        Property_Area=0
    
    
    
        
    
    

# subdata={
#         'Gender':Gender,
#         'Married':Married,
#         'Dependents':Dependents
#         }

    features=[Gender,Married,Dependents,Education,Selfemp,Applicant_Income,Coapplicant_Income,Loanamt,LoanTerm,Credit_history,Property_Area]
    print(features)
    results = np.array(features).reshape(1, -1)

    if st.button("Predict"):
        picklefile = open("emp-model.pkl", "rb")
        model = pickle.load(picklefile)

        prediction = model.predict(results)
        if prediction[0] == 1:
            st.success('Loan will be granted')
        elif prediction[0] == 0:
            st.error( 'Loan will not be granted')