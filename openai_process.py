from openai import OpenAI
from dotenv import load_dotenv
import os

def process_openai(prompt, history, model="gpt-4o-mini"):
    """
    Sends a prompt to the OpenAI API and returns the response.
    Args:
        prompt (str): The input prompt to send to the API.
        model (str): The OpenAI model to use (default is "text-davinci-003").
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

    base_messages = [
        {"role": "developer", "content": "You are a hilarious assistant with a special interest in table tennis."}
    ]
    latest = [
        {"role": "user", "content": prompt}
    ]
    input_combined = base_messages + history + latest
    # print(input_combined)

    try:
        response = client.chat.completions.create(
            model=model,
            store=True,
            messages=input_combined
            # messages=[
            #     {"role": "developer", "content": "You are a hilarious assistant with a special interest in table tennis."},
            #     {"role": "user", "content": prompt}
            # ]
        )
        # response = client.responses.create(
        #     model=model,
        #     previous_response_id=previous_response_id,
        #     input=prompt,
        #     max_tokens=max_tokens
        # )
        # return response.choices[0].message.content

        # print('This should show the response object:')
        # print(response)

        return response
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
