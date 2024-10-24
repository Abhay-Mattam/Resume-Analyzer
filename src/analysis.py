from src.text_extraction import extract_text_from_pdf
from src.text_preprocessing import preprocess_text
from src.skill_extraction import extract_skills

def analyze_resume(resume_path):
    # Extract text from the resume PDF
    resume_text = extract_text_from_pdf(resume_path)
    
    # Preprocess the text (cleaning, tokenizing, lemmatizing)
    processed_text = preprocess_text(resume_text)
    
    # Extract skills by matching against predefined skills
    skills_found = extract_skills(processed_text)
    
    return {
        "skills_matched": skills_found,
        "total_skills": len(skills_found),
    }
