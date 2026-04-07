import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

try:
    # Secrets se load karna
    raw_key = st.secrets["my_key"]
    key_dict = json.loads(raw_key, strict=False) # strict=False se hidden characters ignore ho jate hain
    
    creds = ServiceAccountCredentials.from_json_keyfile_dict(key_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key("1Wu7gvmumWYikaTBGQO41tXeNX8Xh2Sa0lc-Sucb3N20").sheet1

    st.title("Registration Form")
    username = st.text_input("Enter username")
    password = st.text_input("Enter password", type="password")
    
    if st.button("Submit"):
        sheet.append_row([username, password])
        st.success("Success! ✅")
        
except Exception as e:
    st.error(f"Error: {e}")
