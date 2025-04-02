from openai_process import process_openai

def main():
    print(r"""
      ____ _             _     _         
     / ___| |__   __ _ _| |_ _| |_  ___ _ __ 
    | |   | '_ \ / _` |_   _|_   _|/ _ \ '__|
    | |___| | | | (_| | | |   | | |  __/ |
     \____|_| |_|\__,_| |_|   |_|  \___|_|
                                            
    Welcome to Jesse's Docker Chatter CLI!
    """)
    print("Type your input below. Type 'exit' to quit.\n")

    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the loop if the user types 'exit'
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Process the input using the OpenAI API
        if user_input.strip():
            try:
                result = process_openai(user_input)
                print(f"AI: {result}\n")
            except Exception as e:
                print(f"An error occurred: {e}\n")
        else:
            print("Input cannot be empty. Please try again.\n")

if __name__ == "__main__":
    main()