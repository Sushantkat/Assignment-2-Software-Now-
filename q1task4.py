import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
from collections import Counter

# Loading spaCy models
nlp_sci_sm = spacy.load("en_core_sci_sm")
nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")

# Loading BioBert tokenizer and model
tokenizer_biobert = AutoTokenizer.from_pretrained("monologg/biobert_v1.1_pubmed")
model_biobert = AutoModelForTokenClassification.from_pretrained("monologg/biobert_v1.1_pubmed")

# Reading the text from the file
with open("allcsvs.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Function to extract entities using spaCy model
def extract_entities_spacy(nlp_model, text):
    doc = nlp_model(text)
    entities = [ent.text for ent in doc.ents]
    return entities

# Function to extract entities using BioBert model
def extract_entities_biobert(tokenizer, model, text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    predictions = outputs.logits.argmax(dim=2)
    decoded_predictions = [tokenizer.decode(pred) for pred in predictions[0]]
    entities = [token for token, prediction in zip(tokenizer.tokenize(text), decoded_predictions) if prediction != 'O']
    return entities

# Extract entities using spaCy models
entities_sci_sm = extract_entities_spacy(nlp_sci_sm, text)
entities_bc5cdr = extract_entities_spacy(nlp_bc5cdr, text)

# Extract entities using BioBert model
entities_biobert = extract_entities_biobert(tokenizer_biobert, model_biobert, text)

# Count occurrences of entities
counter_sci_sm = Counter(entities_sci_sm)
counter_bc5cdr = Counter(entities_bc5cdr)
counter_biobert = Counter(entities_biobert)

# Calculate common entities
common_entities = set(entities_sci_sm) & set(entities_bc5cdr) & set(entities_biobert)

# Print results
print("Total entities detected by en_core_sci_sm:", len(entities_sci_sm))
print("Total entities detected by en_ner_bc5cdr_md:", len(entities_bc5cdr))
print("Total entities detected by BioBert:", len(entities_biobert))

print("\nCommon entities:")
print(common_entities)

print("\nEntities unique to en_core_sci_sm:")
print(set(entities_sci_sm) - common_entities)

print("\nEntities unique to en_ner_bc5cdr_md:")
print(set(entities_bc5cdr) - common_entities)

print("\nEntities unique to BioBert:")
print(set(entities_biobert) - common_entities)