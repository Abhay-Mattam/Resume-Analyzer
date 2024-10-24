import spacy

# Load spaCy's English model
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    # Process the text using spaCy
    doc = nlp(text.lower())  # Convert to lowercase
    # Lemmatize, remove stop words, and filter out non-alphabetic tokens
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)  # Return the cleaned text as a string
