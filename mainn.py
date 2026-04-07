import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

try:
    # Streamlit Secrets se credentials uthana
    creds_dict = dict(st.secrets["gcp_service_account"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_key("1Wu7gvmumWYikaTBGQO41tXeNX8Xh2Sa0lc-Sucb3N20").sheet1
    
    st.title("Registration Form")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    
    if st.button("Submit"):
        sheet.append_row([u, p])
        st.success("Bhej diya! ✅")
except Exception as e:
    st.error(f"Error: {e}")
