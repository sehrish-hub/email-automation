import streamlit as st
from send_email import send_email

st.title("🚀 AI Job Application System")

st.write("Fill details and send CV instantly")

# Inputs
to_email = st.text_input("HR Email")
designation = st.text_input("Job Title / Designation")
cv_file = st.file_uploader("Upload CV (PDF)", type=["pdf"])

# Button
if st.button("📨 Apply Now"):

    if to_email and designation and cv_file:

        # Save uploaded file
        with open("temp_cv.pdf", "wb") as f:
            f.write(cv_file.read())

        result = send_email(to_email, designation, "temp_cv.pdf")

        st.success(result)

    else:
        st.error("Please fill all fields")
# import streamlit as st
# from scraper import extract_job_data
# from ai_generator import generate_cover_letter
# from email_sender import send_email

# st.title("🚀 AI Auto Job Apply Bot")

# job_url = st.text_input("Paste Job Link")
# skills = st.text_area("Your Skills", "Python, AI, Web Development, Automation")
# to_email = st.text_input("HR Email")
# cv_file = st.file_uploader("Upload CV (PDF)", type=["pdf"])

# if st.button("🚀 Auto Apply"):

#     if job_url and to_email and cv_file:

#         # Save CV
#         with open("temp_cv.pdf", "wb") as f:
#             f.write(cv_file.read())

#         # Extract job info
#         job_title, company = extract_job_data(job_url)

#         # Generate AI cover letter
#         cover_letter = generate_cover_letter(job_title, company, skills)

#         # Send email
#         result = send_email(
#             to_email,
#             f"Application for {job_title}",
#             cover_letter,
#             "temp_cv.pdf"
#         )

#         st.success(result)

#     else:
#         st.error("Fill all fields properly")