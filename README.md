# NLP_Project
# Job Description and Resume Matcher

## Overview

The **Job Description and Resume Matcher** is a Natural Language Processing (NLP) project designed to evaluate and analyze resumes against a given job description. This tool provides similarity scores, sentiment analysis, keyword matching, and experience extraction to help users assess the alignment between job requirements and resumes. Visualizations like bar charts, pie charts, and word clouds provide actionable insights at a glance.

---

## Features

1. **Resume Similarity Scoring**:

   - Calculates similarity between resumes and job descriptions using **TF-IDF Vectorization** and **Cosine Similarity**.

2. **Keyword Matching**:

   - Identifies common keywords between the job description and each resume, highlighting relevant matches.

3. **Sentiment Analysis**:

   - Evaluates the overall sentiment of resumes (positive, neutral, or negative) using **TextBlob**.

4. **Experience Extraction**:

   - Extracts and calculates the total years of experience mentioned in resumes using regular expressions.

5. **Visualizations**:

   - **Bar Chart**: Displays similarity scores for each resume.
   - **Pie Chart**: Summarizes sentiment analysis results.
   - **Word Cloud**: Highlights matched keywords visually.

---

## Installation

### Prerequisites

- Python 3.7+
- pip

### Dependencies

Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

**Required Libraries:**

- `os`
- `re`
- `docx`
- `PyPDF2`
- `matplotlib`
- `wordcloud`
- `nltk`
- `TextBlob`
- `scikit-learn`
- `streamlit`

---

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/job-description-resume-matcher.git
   cd job-description-resume-matcher
   ```

2. **Run the Application:** Start the Streamlit app using the command:

   ```bash
   streamlit run matcher_frontend.py
   ```

3. **Input Data:**

   - Upload one or more resumes (in `.pdf`, `.txt`, `.csv`, or `.docx` formats).
   - Paste the job description into the text box.

4. **View Results:**

   - Get similarity scores, sentiment analysis, keyword matches, and experience details.
   - Explore visualizations for deeper insights.

---

## Project Structure

```
job-description-resume-matcher/
|-- matcher_frontend.py     # Streamlit front-end application
|-- matcher_backend.py      # Backend processing for resumes and job descriptions
|-- requirements.txt        # Python dependencies
|-- README.md               # Project documentation (this file)
|-- sample_data/            # Sample resumes and job descriptions
```

---

## Key Concepts

### 1. **TF-IDF Vectorization**:

- Converts textual data into numerical features based on word importance.

### 2. **Cosine Similarity**:

- Measures textual similarity by calculating the cosine of the angle between two vectors.

### 3. **Sentiment Analysis**:

- Evaluates the polarity of text (positive, neutral, negative).

### 4. **Keyword Matching**:

- Uses set intersections to identify overlapping keywords between job descriptions and resumes.

### 5. **Experience Extraction**:

- Detects years mentioned in resumes and calculates total experience.

---

## Visualizations

### 1. **Bar Chart**

- Displays similarity scores for uploaded resumes, making it easy to identify the best match.

### 2. **Pie Chart**

- Provides an overview of sentiment analysis results.

### 3. **Word Cloud**

- Highlights frequently matched keywords visually, emphasizing the most relevant terms.

---

## Example Results

- **Similarity Scores**:

  - Resume A: 0.75
  - Resume B: 0.62

- **Matched Keywords**:

  - Resume A: Python, Machine Learning, Data Analysis

- **Sentiment Analysis**:

  - Resume A: Positive (0.32)

- **Experience**:

  - Resume A: 3 years

---

## Future Enhancements

- Integration with **Large Language Models** (LLMs) for deeper semantic analysis.
- Support for additional file formats.
- Enhanced visualizations with **interactive dashboards**.
---

## Contributers

- Pavani chella
- Yasaswitha Gaddam

