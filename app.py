import json
import streamlit as st
from resume_parser import extract_text
from utils import clean_text, extract_email, extract_phone, extract_name
from skill_extractor import extract_skills
from section_extractor import (
    extract_projects, extract_achievements,
    extract_education, extract_experience
)

def parse_resume(filepath):
    raw_text = extract_text(filepath)
    clean   = clean_text(raw_text)

    result = {
        "Name":         extract_name(raw_text),
        "Email":        extract_email(raw_text),
        "Phone":        extract_phone(raw_text),
        "Skills":       extract_skills(clean),
        "Projects":     extract_projects(raw_text),
        "Achievements": extract_achievements(raw_text),
        "Education":    extract_education(raw_text),
        "Experience":   extract_experience(raw_text),
    }
    return result

# ── Streamlit UI ──────────────────────────────────────────────
st.set_page_config(page_title="AI Resume Screener", page_icon="📄")
st.title("📄 AI Resume Screening System")
st.write("Upload a resume in PDF or DOCX format to extract structured information.")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:
    # Save temp file
    temp_path = f"temp_{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Analyzing resume..."):
        data = parse_resume(temp_path)

    st.success("Resume parsed successfully!")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("👤 Personal Details")
        st.write(f"**Name:** {data['Name']}")
        st.write(f"**Email:** {data['Email']}")
        st.write(f"**Phone:** {data['Phone']}")

    with col2:
        st.subheader("🛠️ Skills")
        if data["Skills"]:
            st.write(", ".join(data["Skills"]))
        else:
            st.write("No skills detected.")

    st.subheader("📁 Projects")
    for p in data["Projects"]:
        st.markdown(f"- {p}")

    st.subheader("🏆 Achievements")
    for a in data["Achievements"]:
        st.markdown(f"- {a}")

    st.subheader("📚 Education")
    for e in data["Education"]:
        st.markdown(f"- {e}")

    st.subheader("💼 Experience")
    for x in data["Experience"]:
        st.markdown(f"- {x}")

    st.subheader("📦 Raw JSON Output")
    st.json(data)