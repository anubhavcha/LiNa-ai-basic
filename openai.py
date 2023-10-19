# 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

import openai

# Replace 'YOUR_API_KEY' with your OpenAI API key
api_key = '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'

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_response(prompt):
    try:
        # Generate a response using the OpenAI API
        response = openai.Completion.create(
            engine="davinci-codex",  # You can choose different engines depending on your needs
            prompt=prompt,
            max_tokens=50  # You can adjust the maximum response length
        )

        # Extract and return the generated text
        return response.choices[0].text.strip()

    except Exception as e:
        return str(e)

# Main loop to take user input and generate responses
print("Chatbot: Hello! How can I assist you today? (Type 'exit' to end the conversation)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ['exit', 'quit']:
        print("Chatbot: Goodbye!")
        break

    # Generate a response based on user input
    bot_response = generate_response(user_input)

    print("Chatbot:", bot_response)
