import streamlit as st
from courses import courses


def register_student():
    st.title("ثبت نام")
    name = st.text_input("نام")
    lname = st.text_input("نام خانوادگی")
    course = [corse["title"] for corse in courses]
    choice = st.selectbox("Select an option", course)

    if st.button("Register"):
        if name and lname and choice:
            st.success(f"{name} {lname} شما در دوره  {choice}  ثبت نام  شدید ")
        else:
            st.error("Please fill in all fields.")
