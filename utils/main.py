from model.nmt_model import NMTModel
from utils.preprocessing import clean_text, preprocess_pipeline
from train import train
from evaluate import evaluate


def interactive_mode(model):
    print("\n" + "=" * 40)
    print("Interactive Translation Mode")
    print("Type 'exit' to quit")
    print("=" * 40)

    while True:
        user_input = input("\nEnter text to translate: ")

        if user_input.lower() == "exit":
            print("Exiting interactive mode...")
            break

        processed = preprocess_pipeline(user_input)
        translation = model.translate(processed["clean"])

        print("Clean Text:", processed["clean"])
        print("Tokens:", processed["tokens"])
        print("Translation:", translation)


def show_menu():
    print("\n" + "=" * 40)
    print("NMT Technical Specifications System")
    print("=" * 40)
    print("1. Train Model")
    print("2. Evaluate Model")
    print("3. Interactive Translation")
    print("4. Show Dictionary")
    print("0. Exit")


def main():
    model = NMTModel()

    while True:
        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            train()

        elif choice == "2":
            evaluate()

        elif choice == "3":
            interactive_mode(model)

        elif choice == "4":
            model.show_dictionary()

        elif choice == "0":
            print("Exiting system...")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
