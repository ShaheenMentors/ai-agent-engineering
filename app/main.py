from app.ai_client import ask_ai

def main():
    while True:
        question = input("Ask the AI: ")
        if question.lower() == "exit":
            print("Goodbye")
            break
        elif not question.strip():
            print("Please enter a question or Type 'exit' to quit")
            continue
        try:
            answer = ask_ai(question)
            print(answer) 
        except Exception as error:
            print(f"Server Error: {error}")

if __name__ == "__main__":
    main()
