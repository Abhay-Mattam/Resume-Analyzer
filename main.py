from src.analysis import analyze_resume

def main():
    # Ask user for the resume file path
    resume_path = input("Enter the path to the resume (PDF): ")
    
    # Analyze the resume
    analysis_result = analyze_resume(resume_path)
    
    # Display the analysis results
    print(f"Skills Matched: {analysis_result['skills_matched']}")
    print(f"Total Skills Found: {analysis_result['total_skills']}")

if __name__ == "__main__":
    main()
