# Predefined list of important skills
skills = ['python', 'machine learning', 'data analysis', 'ai', 'deep learning', 'communication', 'teamwork']

def extract_skills(resume_text):
    # Tokenize resume text
    resume_words = set(resume_text.split())  # Split text into words and remove duplicates using a set
    # Match skills from the predefined list
    matched_skills = [skill for skill in skills if skill in resume_words]
    return matched_skills
