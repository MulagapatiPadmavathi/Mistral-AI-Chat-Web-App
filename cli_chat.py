from api_integration import get_response

def chat():
    """Interactive CLI chatbot using Mistral API."""
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break

        response = get_response(user_input)
        print(f"Mistral AI: {response}")

if __name__ == "__main__":
    chat()
