# app/ml.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(user_skills, job_description):
    """Calculate similarity between user skills and job description."""
    vectorizer = TfidfVectorizer().fit_transform([user_skills, job_description])
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    return cosine_sim[0][1]  # Return the similarity score
