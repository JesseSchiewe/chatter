from openai_process import process_openai

def main():
    # This is used to track previous responses to allow for context in the conversation.
    history = []

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
            print("Goodbye from Chatter!")
            break

        # Process the input using the OpenAI API
        if user_input.strip():
            try:
                result = process_openai(user_input, history)
                print(f"ChatterAI: {result.choices[0].message.content}\n")

                for item in result.choices:
                    history.append({"role": item.message.role, "content": item.message.content})
            
            except Exception as e:
                print(f"An error occurred: {e}\n")
        else:
            print("Input cannot be empty. Please try again.\n")

if __name__ == "__main__":
    main()