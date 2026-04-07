import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Google Sheet connect setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Secrets se 'my_key' wala data uthana
key_dict = json.loads(st.secrets["my_key"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(key_dict, scope)
client = gspread.authorize(creds)

# Sheet ID se connect karna (Ye sabse best hai)
sheet = client.open_by_key("1Wu7gvmumWYikaTBGQO41tXeNX8Xh2Sa0lc-Sucb3N20").sheet1

# UI Part
st.title("Registration Form")

username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")
followers = st.text_input("Followers")
age = st.number_input("Age", min_value=1, max_value=100)

if st.button("Submit"):
    sheet.append_row([username, password, followers, age])
    st.success("Data saved successfully! ✅")
