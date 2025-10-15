import streamlit as st

# Website Title and Header
st.title("SP Coaching Classes")
st.subheader("Learn, Grow, and Succeed with Us")

st.write("""
Welcome to **SP Coaching Classes**, your trusted learning partner for 
students from class 6th to 12th and competitive exams like NEET, JEE, and SSC.
""")

# Add an image (optional)
st.image("https://cdn.pixabay.com/photo/2015/09/05/20/02/classroom-925595_960_720.jpg", 
         caption="SP Coaching Classroom", use_container_width=True)

# Sidebar Navigation
menu = st.sidebar.radio("ABOUT", ["Home", "Courses Offered", "Institute Details", "Student Enrollment"])

# 1️⃣ Home Page
if menu == "Home":
    st.header("Welcome to sp Coaching Classes")
    st.write("""
    SP Coaching Classes is committed to providing quality education 
    and personal guidance to students.  
    Our experienced faculty ensures conceptual clarity and exam-oriented preparation.
    """)

# 2️⃣ Courses Offered
elif menu == "Courses Offered":
    st.header("📚 Courses Offered")
    st.write("""
    We provide coaching for:
    - Class 6th to 10th (All Subjects)
    - Class 11th & 12th (Science / Commerce / Arts)
    - NEET / JEE Preparation
    """)

    st.info("Special Batch for 10th & 12th Board Students starting soon!")

# 3️⃣ CLASSES Details
elif menu == "CLASSES Details":
    st.header(" CLASSES Details")
    st.write("""
    **CLASSES Name:** RS Coaching Classes  
    **Address:** Near Main Market, Civil Lines, [Your City Name]  
    **Contact:** +91 98765 43210  
    **Email:** SPcoaching@gmail.com  
    **Timings:** Monday to Saturday - 8:00 AM to 7:00 PM  
    **Head:** Mr. P. Sharma (Founder & Director)
    """)

# 4️⃣ Student Enrollment Page
elif menu == "Student Enrollment":
    st.header("🧾 Student Enrollment Form")
    st.write("Please fill the form below to register:")

    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=10, max_value=60, step=1)
    course = st.selectbox("Select Course", 
                          ["Class 6th-10th", "Class 11th", "Class 12th", "NEET", "JEE", "SSC"])
    contact = st.text_input("Contact Number")
    email = st.text_input("Email ID")
    address = st.text_area("Address")

    if st.button("Submit"):
        if name and contact and course:
            st.success(f"Thank you {name}! You have successfully enrolled for {course}.")
            st.balloons()
        else:
            st.error("Please fill all mandatory fields before submitting.")