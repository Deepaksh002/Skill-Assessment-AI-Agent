import streamlit as st
from utils import (
    read_pdf,
    extract_skills,
    evaluate_skill,
    match_skills,
    generate_learning_plan
)

st.set_page_config(page_title="AI Skill Agent", layout="wide")

st.title("🤖 AI Skill Assessment & Learning Agent")

# -------- INPUT --------
jd = st.text_area("📄 Paste Job Description")
resume_file = st.file_uploader("📎 Upload Resume (PDF)")

# -------- PROCESS --------
if st.button("🚀 Analyze Candidate"):

    if not jd or not resume_file:
        st.warning("Please provide both JD and Resume")
        st.stop()

    # Read resume
    with st.spinner("Reading resume..."):
        resume_text = read_pdf(resume_file)

    # Extract skills
    with st.spinner("Extracting skills..."):
        jd_skills = extract_skills(jd)
        resume_skills = extract_skills(resume_text)

    # Display skills
    st.subheader("🧠 Extracted Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**JD Skills**")
        st.write(jd_skills)

    with col2:
        st.write("**Resume Skills**")
        st.write(resume_skills)

    # Match skills
    matched, missing = match_skills(jd_skills, resume_skills)

    st.subheader("🔍 Skill Analysis")
    st.write("✅ Matched Skills:", matched)
    st.write("❌ Missing Skills:", missing)

    # Evaluate skills
    st.subheader("📊 Skill Scores")

    scores = {}

    for skill in jd_skills[:5]:  # limit for speed
        with st.spinner(f"Evaluating {skill}..."):
            score, explanation = evaluate_skill(skill)
            scores[skill] = score

            st.write(f"### {skill}")
            st.write(f"Score: **{score}/5**")
            st.write(explanation)

    # Learning plan
    st.subheader("📚 Personalized Learning Plan")

    with st.spinner("Generating plan..."):
        plan = generate_learning_plan("Target Role", missing)

    st.write(plan)