import spacy
import inflect

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Initialize inflect engine
p = inflect.engine()

# Irregular noun dictionary
IRREGULARS = {
    "children": "child",
    "men": "man",
    "women": "woman",
    "mice": "mouse",
    "teeth": "tooth",
    "feet": "foot"
}


# -------------------------------
# Convert plural nouns to singular
# -------------------------------
def convert_to_singular(text):
    doc = nlp(text)
    output = []

    for token in doc:
        if token.pos_ == "NOUN":
            word = token.text.lower()

            if word in IRREGULARS:
                output.append(IRREGULARS[word])
            else:
                singular = p.singular_noun(token.text)
                output.append(singular if singular else token.text)
        else:
            output.append(token.text)

    return " ".join(output)


# -------------------------------
# Convert singular nouns to plural
# -------------------------------
def convert_to_plural(text):
    doc = nlp(text)
    output = []

    for token in doc:
        if token.pos_ == "NOUN":
            output.append(p.plural(token.text))
        else:
            output.append(token.text)

    return " ".join(output)


# -------------------------------
# Extract root words (lemmatization)
# -------------------------------
def extract_root_words(text):
    doc = nlp(text)
    roots = []

    for token in doc:
        if token.is_alpha and not token.is_stop:
            roots.append(token.lemma_)

    return roots