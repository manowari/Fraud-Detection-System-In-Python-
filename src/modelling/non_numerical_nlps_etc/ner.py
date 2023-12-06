# Import necessary libraries
import spacy
import pandas as pd

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Function for Named Entity Recognition
def perform_ner(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example usage
text_data = ["An unauthorized access attempt was detected in account #123456.", "Transaction of $1000 made by John Doe."]
for text in text_data:
    entities = perform_ner(text)
    print(f"Entities in '{text}': {entities}")
