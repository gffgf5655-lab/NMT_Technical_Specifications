from model.nmt_model import NMTModel
from utils.preprocessing import clean_text, tokenize_text

def load_data():
    print("Loading technical specifications dataset...")

    dataset = [
        "The processor operates at 3.2 GHz.",
        "The system uses a cooling fan.",
        "The device supports multiple connections.",
        "The motherboard connects all components."
    ]

    return dataset


def preprocess_dataset(dataset):
    print("Preprocessing dataset...")

    processed = []

    for text in dataset:
        clean = clean_text(text)
        tokens = tokenize_text(clean)
        processed.append({
            "original": text,
            "clean": clean,
            "tokens": tokens
        })

    return processed


def train():
    print("=" * 40)
    print("Starting NMT Training Pipeline")
    print("=" * 40)

    model = NMTModel()

    dataset = load_data()
    processed_data = preprocess_dataset(dataset)

    print("\nTraining on samples:\n")

    for sample in processed_data:
        translated = model.translate(sample["clean"])

        print("Input:", sample["original"])
        print("Clean:", sample["clean"])
        print("Tokens:", sample["tokens"])
        print("Output:", translated)
        print("-" * 40)

    print("Training completed successfully!")


if __name__ == "__main__":
    train()
