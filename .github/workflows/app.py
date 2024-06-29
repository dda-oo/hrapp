# app.py
import streamlit as st
from utils import extract_text_from_pdf, compare_text

# Streamlit app setup
st.title("Candidate Matching App")

st.header("Upload Your CV and Enter Job Description")
st.write("Upload your CV as a PDF file or provide a LinkedIn URL. Enter the job description text from the job ad.")

# Upload PDF CV
cv_file = st.file_uploader("Upload CV PDF", type="pdf")

# Enter LinkedIn URL (optional)
cv_link = st.text_input("LinkedIn URL (Optional)")

# Enter Job Description
job_description = st.text_area("Job Description Text")

if st.button("Compare"):
    if cv_file:
        # Extract text from PDF CV
        cv_text = extract_text_from_pdf(cv_file)
    elif cv_link:
        st.warning("LinkedIn URL extraction is not implemented in this demo. Please use the PDF option.")
        cv_text = "Sample CV Text from LinkedIn (Mock)"
    else:
        st.error("Please upload a PDF CV or provide a LinkedIn URL.")
        cv_text = ""

    if not job_description:
        st.error("Please enter the job description text.")
    else:
        # Compare CV and Job Description
        percentage, color, hint = compare_text(cv_text, job_description)

        # Display Results
        st.subheader(f"Match Likelihood: {percentage:.2f}%")
        st.markdown(f"<div style='background-color: {color}; padding: 10px; border-radius: 5px;'>{hint}</div>", unsafe_allow_html=True)
