import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheet connect
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("flawless-mason-492603-t0-0db917a2263e.json", scope)
client = gspread.authorize(creds)

sheet = client.open_by_key("1Wu7gvmumWYikaTBGQO41tXeNX8Xh2Sa0Ic-Sucb3N20").sheet1

# UI
st.title("Form")

username = st.text_input("Enter username")
password = st.text_input("Enter password")
followers = st.text_input("Followers")
age = st.number_input("Age")

if st.button("Submit"):
    sheet.append_row([username, password, followers, age])
    st.success("Data saved ✅")
