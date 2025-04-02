from openai import OpenAI
from dotenv import load_dotenv
import os
# from sys import argv

# Handle input passed to the script
# input_prompt = argv[1]
# print(f'##### Sending this to OpenAI API: {input_prompt}')
# print('')

def process_openai(prompt, model="gpt-4o-mini", max_tokens=150):
    """
    Sends a prompt to the OpenAI API and returns the response.

    Args:
        prompt (str): The input prompt to send to the API.
        model (str): The OpenAI model to use (default is "text-davinci-003").
        max_tokens (int): The maximum number of tokens to include in the response.

    Returns:
        str: The response from the OpenAI API.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Access the API key from the environment
    openai_api_key = os.getenv("OPENAIAPIKEY")

    client = OpenAI(
        api_key=openai_api_key
    )
    
    try:
        response = client.chat.completions.create(
            model=model,
            store=True,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    if len(argv) > 1:
        print('Running process_openai function...')
        response = process_openai(input_prompt)
        print(response)
    else:
        print('Please provide a prompt to send to the OpenAI API.')

# if __name__ != "__main__":
#     print('This is not the main module.')
