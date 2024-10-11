import streamlit as st
from courses import courses
from registration import register_student
from exercises import coding_exercise


def main():
    st.title("💻خانه برنامه نویسان اهواز")
    st.write("👨‍💻با مدیریت جمشید افشانی", )

    
    menu = ["صفحه اصلی", "دوره ها", "ثبت نام", "تمرین"]
    choice = st.sidebar.selectbox("Select an option", menu)
    
    if choice == "صفحه اصلی":
        st.write("به خانه برنامه نویسان اهواز خوش آمدید")
    
    elif choice == "دوره ها":
        st.write("دوره های فعال:")
        for course in courses:
            st.subheader(course["title"])
            st.write(course["توضیحات دوره"])
            st.write(f"مدت زمان دوره: {course['مدت زمان']}")
    
    elif choice == "ثبت نام":
        register_student()
    
    elif choice == "تمرین":
        coding_exercise()

if __name__ == "__main__":
    main()
