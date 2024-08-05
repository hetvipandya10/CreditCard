import streamlit as st

st.title("Welcome to Creditcard App")

Time=st.slider("Select Time=",20,80)
V1=st.slider("Select V1=",0,1)
V2=st.slider("Select V2=",15,39)
V3=st.slider("Select V3=",0,1)
V4=st.slider("Select V4=",0,2)
V5=st.slider("Select V5=",0,9)
V6=st.slider("Select V6=",0,1)
V7=st.slider("Select V7=",0,1)
V8=st.slider("Select V8=",1,2)
V9=st.slider("Select V9=",7,1)
V10=st.slider("Select V10=",7,6)
V11=st.slider("Select V11=",2,6)
V12=st.slider("Select V12=",4,1)
V13=st.slider("Select V13=",12,6)
V14=st.slider("Select V14=",67,21)
V15=st.slider("Select V15=",7,1)
V16=st.slider("Select V16=",9,21)
V17=st.slider("Select V17=",10,1)
V18=st.slider("Select V18=",10,6)
V19=st.slider("Select V19=",8,9)
V20=st.slider("Select V20=",4,21)
V21=st.slider("Select V21=",5,2)
V22=st.slider("Select V22=",8,9)
V23=st.slider("Select V23=",7,2)
V24=st.slider("Select V24=",3,9)
V25=st.slider("Select V25=",3,2)
V26=st.slider("Select V26=",10,1)
V27=st.slider("Select V27=",7,6)
V28=st.slider("Select V28=",17,16)
Amount=st.slider("Select Amount=",67,16)
Class=st.slider("Select Class=",45,34)


if st.button("Predict"):
    import pickle
    model=pickle.load(open("Creditcard.pkl","rb"))
    prd=model.predict([[Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28]])
    st.success("The Creditcard is "+ str(prd[0]))

