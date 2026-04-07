import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

try:
    # Seedha dictionary uthana secrets se
    creds_dict = dict(st.secrets["gcp_service_account"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    
    # Sheet name check kar lena "harsh the hacker" ya jo bhi hai
    sheet = client.open_by_key("1Wu7gvmumWYikaTBGQO41tXeNX8Xh2Sa0lc-Sucb3N20").sheet1
    
    st.title("Registration Form")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    
    if st.button("Submit"):
        sheet.append_row([u, p])
        st.success("Done! ✅")
except Exception as e:
    st.error(f"Error: {e}")
