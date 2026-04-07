import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# secrets se credentials lena
creds_dict = st.secrets["gcp_service_account"]

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1Wu7gvmumWYikaTBGQO41tXeNX8Xh2Sa0Ic-Sucb3N20/edit?gid=0#gid=0").sheet1

st.title("Form")

username = st.text_input("Enter username")
password = st.text_input("Enter password")
followers = st.text_input("Followers")
age = st.number_input("Age")

if st.button("Submit"):
    sheet.append_row([username, password, followers, age])
    st.success("Data saved ✅")
