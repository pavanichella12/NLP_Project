import streamlit as st
import os
from matcher_backend import process_resumes, extract_keywords, analyze_sentiment, calculate_experience, generate_visualizations

# Set up the Streamlit app
st.set_page_config(page_title="Resume Matcher", layout="wide", page_icon="🔍")

# Header
st.title("🔍 Job Description and Resume Matcher")
st.markdown("**Easily compare resumes to a job description and get detailed insights, scores, and visualizations.**")
st.divider()

# Upload and Input Section
with st.container():
    st.header("Upload Resumes and Enter Job Description")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        uploaded_files = st.file_uploader(
            "Upload Resumes (PDF, DOCX, TXT, CSV)", 
            type=["csv", "txt", "pdf", "docx"], 
            accept_multiple_files=True
        )
    
    with col2:
        job_description = st.text_area("Enter Job Description", "Type or paste the job description here...")
    
    st.divider()

# Validation and Processing
if uploaded_files and job_description.strip():
    st.success(f"Uploaded {len(uploaded_files)} resume(s): {', '.join([file.name for file in uploaded_files])}")

    if st.button("🔄 Process Resumes"):
        with st.spinner("⏳ Processing resumes... This might take a moment."):
            try:
                # Save uploaded files temporarily
                file_paths = []
                for file in uploaded_files:
                    temp_file_path = f"temp_{file.name}"
                    with open(temp_file_path, "wb") as f:
                        f.write(file.getbuffer())
                    file_paths.append(temp_file_path)

                # Process resumes and gather insights
                results = process_resumes(file_paths, job_description)
                keywords_matched = extract_keywords(file_paths, job_description)
                sentiment_scores = analyze_sentiment(file_paths)
                experience_info = calculate_experience(file_paths)

                # Display Results Section by Section
                st.success("✅ Processing Complete!")
                st.subheader("Similarity Scores")
                for result in results:
                    st.markdown(f"**Resume:** {result['file_name']} - **Score:** {result['similarity_score']:.2f}")

                with st.expander("📊 Keyword Matches", expanded=True):
                    for file_name, keywords in keywords_matched.items():
                        st.markdown(f"**Resume:** {file_name}")
                        st.write(f"Matched Keywords: {', '.join(keywords)}")

                with st.expander("🧠 Sentiment Analysis"):
                    for file_name, sentiment in sentiment_scores.items():
                        st.markdown(f"**Resume:** {file_name} - **Sentiment Score:** {sentiment:.2f}")

                with st.expander("📜 Experience Information"):
                    for file_name, experience in experience_info.items():
                        st.markdown(f"**Resume:** {file_name} - **Extracted Experience:** {experience}")

                # Display Visualizations
                st.header("📈 Visualizations")
                bar_chart, pie_chart, word_cloud = generate_visualizations(results, sentiment_scores, keywords_matched)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write("### Similarity Scores Bar Chart")
                    st.pyplot(bar_chart)
                with col2:
                    st.write("### Sentiment Analysis Pie Chart")
                    st.pyplot(pie_chart)
                with col3:
                    st.write("### Keyword Matches Word Cloud")
                    st.pyplot(word_cloud)

                # Cleanup temporary files
                for path in file_paths:
                    os.remove(path)
                
            except Exception as e:
                st.error(f"🚨 An error occurred: {str(e)}")
else:
    st.warning("⚠️ Please upload resumes and provide a job description to proceed.")
