import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

try:
    # Direct key.json file se credentials lena
    creds = ServiceAccountCredentials.from_json_keyfile_name("key.json", scope)
    client = gspread.authorize(creds)
    
    # Aapki Sheet open karna
    sheet = client.open_by_key("1Wu7gvmumWYikaTBGQO41tXeNX8Xh2Sa0lc-Sucb3N20").sheet1
    
    st.title("Form")
    u = st.text_input("Enter username")
    p = st.text_input("Enter password", type="password")
    
    if st.button("Submit"):
        sheet.append_row([u, p])
        st.success("Saved successfully! ✅")
except Exception as e:
    st.error(f"Error: {e}")
