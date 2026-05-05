from model.nmt_model import NMTModel
from utils.preprocessing import clean_text

def evaluate():
    print("=" * 40)
    print("Evaluating NMT Model")
    print("=" * 40)

    model = NMTModel()

    test_sentences = [
        "The processor operates at 3.2 GHz",
        "The system uses a cooling fan",
        "The device supports multiple connections",
        "The system has advanced features"
    ]

    for sentence in test_sentences:
        clean = clean_text(sentence)
        translation = model.translate(clean)

        print("\nInput:", sentence)
        print("Clean:", clean)
        print("Translation:", translation)

    print("\nEvaluation completed!")


if __name__ == "__main__":
    evaluate()
