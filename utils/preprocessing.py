import re

def clean_text(text):
    text = text.lower()
    text = remove_extra_spaces(text)
    text = remove_symbols(text)
    return text

def remove_extra_spaces(text):
    return " ".join(text.split())

def remove_symbols(text):
    return re.sub(r"[^a-zA-Z0-9\s.]", "", text)

def tokenize_text(text):
    return text.split()

def remove_stopwords(tokens):
    stopwords = ["the", "is", "at", "a", "an"]
    return [word for word in tokens if word not in stopwords]

def preprocess_pipeline(text):
    clean = clean_text(text)
    tokens = tokenize_text(clean)
    filtered = remove_stopwords(tokens)

    return {
        "clean": clean,
        "tokens": tokens,
        "filtered": filtered
    }

def print_preprocessing_steps(text):
    result = preprocess_pipeline(text)

    print("Original:", text)
    print("Clean:", result["clean"])
    print("Tokens:", result["tokens"])
    print("Filtered:", result["filtered"])
