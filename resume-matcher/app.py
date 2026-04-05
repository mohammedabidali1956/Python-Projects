import streamlit as st
from utils import calculate_similarities, get_missing_skills ,get_matched_skills
from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text+= page.extract_text()
    return text

st.title("AI Resume ↔ Job Description Matcher")
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume_file and jd_text:
        resume_text = extract_text_from_pdf(resume_file)
        score = calculate_similarities(resume_text, jd_text)
        missing = get_missing_skills(resume_text, jd_text)
        matched = get_matched_skills(resume_text, jd_text)
        st.subheader("Matched Skills")
        st.write(matched)

        st.subheader(f"Match Score: {score}%")
        st.subheader("Missing Keywords")
        st.write(missing)

    else:
        st.warning("Please upload Resume and Job Description")