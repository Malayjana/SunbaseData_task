import pickle
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title=" Customer Churn Prediction",
    layout="centered"
)

model = pickle.load(open("Downloads/model", 'rb'))

def main():
   
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Customer Churn Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    Age = st.text_input("Age")
    Gender = st.text_input("Gender")
    Subscription_Length_Months = st.text_input("Subscription_Length_Months")
    Monthly_Bill = st.text_input("Monthly_Bill")
    Total_Usage_GB = st.text_input("Total_Usage_GB")
    Location_Chicago = st.text_input("Location_Chicago")
    Location_Houston = st.text_input("Location_Houston")
    Location_Los_Angeles = st.text_input("Location_Los_Angeles")
    Location_Miami = st.text_input("Location_Miami")
    Location_New_York = st.text_input("Location_New_York")
    
    result=''
    if st.button("Predict"):
        res=model.predict([[Age,Gender,Subscription_Length_Months,Monthly_Bill,Total_Usage_GB,Location_Chicago,Location_Houston,Location_Los_Angeles,Location_Miami,Location_New_York]])
        if (res[0]==1):
            result = 'churn'
        else:
            result = 'not churn'
    st.success(result)
    

if __name__=='__main__':
    main()