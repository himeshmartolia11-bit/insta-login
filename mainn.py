import    streamlit as st
import pandas as pd

name = st.text_input("enter your username :  ")
fname = st.text_input("enter your password : ")
adr   = st.text_area ("enter the number of following you need ")
classdata = st.selectbox ("Enter your age :",(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,18))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Father Name :{fname}
    address : {classdata}""")