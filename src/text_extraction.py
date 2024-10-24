from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from the first page of a given PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the first page.
    """
    try:
        # Open and read the PDF file
        reader = PdfReader(pdf_path)
        
        # Extract text from the first page
        if len(reader.pages) > 0:
            page = reader.pages[0]
            extracted_text = page.extract_text()
            return extracted_text if extracted_text else "No text found on the first page."
        else:
            return "No pages found in the PDF."
    
    except Exception as e:
        return f"Error occurred: {e}"

