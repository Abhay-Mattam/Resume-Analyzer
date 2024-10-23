from flask import Flask, render_template, request
from src.text_extraction import extract_text_from_pdf  # Import your PDF text extraction function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400

    # Save the uploaded file to a temporary path
    file_path = f"./uploads/{file.filename}"
    file.save(file_path)
    
    # Analyze the uploaded resume using the function
    extracted_text = extract_text_from_pdf(file_path)
    
    # Display the result on a new webpage
    return render_template('result.html', text=extracted_text)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
