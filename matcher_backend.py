import os
import re
import docx
import PyPDF2
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download("stopwords")
nltk.download("punkt")

stop_words = set(stopwords.words("english"))


def read_file(file_path):
    try:
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        elif file_path.endswith(".docx"):
            doc = docx.Document(file_path)
            return "\n".join([p.text for p in doc.paragraphs])
        elif file_path.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(file_path)
            return " ".join([page.extract_text() for page in pdf_reader.pages])
    except Exception:
        return ""
    return ""


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words and word.isalpha()]
    return " ".join(tokens)


def process_resumes(file_paths, job_description):
    preprocessed_job_desc = preprocess_text(job_description)
    resumes, file_names = [], []
    for file_path in file_paths:
        resume_text = preprocess_text(read_file(file_path))
        resumes.append(resume_text)
        file_names.append(os.path.basename(file_path))

    all_text = [preprocessed_job_desc] + resumes
    vectorizer = TfidfVectorizer(max_features=1000)
    vectors = vectorizer.fit_transform(all_text)
    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    return [{"file_name": file_name, "similarity_score": round(score, 2)} for file_name, score in zip(file_names, similarity_scores)]


def extract_keywords(file_paths, job_description):
    job_keywords = set(preprocess_text(job_description).split())
    matched_keywords = {}
    for file_path in file_paths:
        resume_keywords = set(preprocess_text(read_file(file_path)).split())
        matched_keywords[os.path.basename(file_path)] = job_keywords.intersection(resume_keywords)
    return matched_keywords


def analyze_sentiment(file_paths):
    sentiment_scores = {}
    for file_path in file_paths:
        resume_text = read_file(file_path)
        sentiment_scores[os.path.basename(file_path)] = TextBlob(resume_text).sentiment.polarity
    return sentiment_scores


def calculate_experience(file_paths):
    experience_info = {}
    for file_path in file_paths:
        resume_text = read_file(file_path)
        years = re.findall(r"\b\d{4}\b", resume_text)
        if years:
            min_year, max_year = min(map(int, years)), max(map(int, years))
            experience_info[os.path.basename(file_path)] = f"{max_year - min_year} years" if max_year > min_year else "N/A"
        else:
            experience_info[os.path.basename(file_path)] = "N/A"
    return experience_info



# Generate visualizations with smaller sizes and sorted results
def generate_visualizations(results, sentiment_scores, keywords_matched):
    # Bar chart for similarity scores
    fig1, ax1 = plt.subplots(figsize=(8, 4))  # Adjust size
    ax1.bar(
        [res["file_name"] for res in results],
        [res["similarity_score"] for res in results],
        color="skyblue"
    )
    ax1.set_title("Similarity Scores")
    ax1.set_xlabel("Resumes")
    ax1.set_ylabel("Scores")
    ax1.tick_params(axis="x", rotation=45)

    # Pie chart for sentiment analysis
    fig2, ax2 = plt.subplots(figsize=(5, 5))  # Adjust size
    sentiment_values = list(sentiment_scores.values())
    labels = ["Positive", "Neutral", "Negative"]
    positive = len([s for s in sentiment_values if s > 0.1])
    neutral = len([s for s in sentiment_values if -0.1 <= s <= 0.1])
    negative = len([s for s in sentiment_values if s < -0.1])
    ax2.pie(
        [positive, neutral, negative],
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )
    ax2.set_title("Sentiment Analysis")

    # Word cloud for keyword matches
    fig3, ax3 = plt.subplots(figsize=(8, 4))  # Adjust size
    all_keywords = " ".join([word for keywords in keywords_matched.values() for word in keywords])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_keywords)
    ax3.imshow(wordcloud, interpolation="bilinear")
    ax3.axis("off")
    ax3.set_title("Keyword Matches Word Cloud")

    return fig1, fig2, fig3


