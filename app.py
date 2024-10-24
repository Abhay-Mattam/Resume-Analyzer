# from flask import Flask, render_template, request
# from src.text_extraction import extract_text_from_pdf  # Import your PDF text extraction function

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_resume():
#     if 'file' not in request.files:
#         return "No file uploaded", 400
    
#     file = request.files['file']
    
#     if file.filename == '':
#         return "No selected file", 400

#     # Save the uploaded file to a temporary path
#     file_path = f"{file.filename}"
#     file.save(file_path)
    
#     # Analyze the uploaded resume using the function
#     extracted_text = extract_text_from_pdf(file_path)
    
#     # Display the result on a new webpage
#     return render_template('result.html', text=extracted_text)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
from src.analysis import analyze_resume  # Import the analyze_resume function
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return "No resume file uploaded", 400

    resume_file = request.files['resume']
    
    if resume_file.filename == '':
        return "No selected file", 400

    # Save the uploaded resume to a temporary path
    resume_path = os.path.join('uploads', resume_file.filename)
    os.makedirs('uploads', exist_ok=True)
    resume_file.save(resume_path)

    # Analyze the uploaded resume using the function from main.py
    analysis_result = analyze_resume(resume_path)

    # Clean up the saved file after analysis if needed
    os.remove(resume_path)

    # Render the result on a new webpage
    return render_template(
        'result.html', 
        skills_matched=analysis_result['skills_matched'],
        total_skills=analysis_result['total_skills']
    )

if __name__ == "__main__":
    app.run(debug=True)
