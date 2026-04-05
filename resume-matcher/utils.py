from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def calculate_similarities(resume, jd):
    text = [resume, jd]
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(text)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(similarity[0][0] * 100, 2)

def get_keywords(text):
    text = text.lower()
    # remove punctuations
    text = re.sub(r'[^a-zA-Z0-9\s]', '',text)
    words = text.split()

    stop_words = {
       "the","is","and","in","on","at","of","to","we","are","have","should",
       "with","for","a","an","our","this","that","as","be","by"}
    
    filtered = [word for word in words if word not in stop_words]
    return set(filtered)

COMMON_SKILLS = {
    "python","ml","machine","learning","sql","numpy","pandas",
    "scikit","tensorflow","pytorch","nlp","data","analysis",
    "algorithms","git","github"
}

def get_missing_skills(resume, jd):
    resume_words = get_keywords(resume)
    jd_words = get_keywords(jd)
    jd_skills = jd_words & COMMON_SKILLS
    resume_skills = resume_words & COMMON_SKILLS

    missing_words = jd_skills - resume_skills
    return list(missing_words)

def get_matched_skills(resume, jd):
    resume_words = get_keywords(resume)
    jd_words = get_keywords(jd)
    jd_skills = jd_words & COMMON_SKILLS
    resume_skill = resume_words & COMMON_SKILLS

    matched = jd_skills & resume_skill
    return(matched)