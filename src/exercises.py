# exercises.py
import streamlit as st

def coding_exercise():
    st.title("تمرین کدنویسی")
    code = st.text_area("کد خود را در باکس زیر وارد کنید:")
    
    if st.button("Run Code"):
        try:
            #میخوام که کدش  سیو یا به جایی ارسال بشه
            exec(code)
        except Exception as e:
            st.error(f"Error: {e}")
