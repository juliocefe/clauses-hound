import openai
import os

# indications = """
# This is an app to detect the most sensitive or critical clause.
# Give me the answer based on the instructions I am giving you, nothing more.
# Instructiones:
# The answer in spanish.
# Format:
# "The clause, your explanation about what this is the most critical an sensitive clause."
# """
indications = """
This is an app to summary a contract obligations.
Give me the answer based on the instructions I am giving you, nothing more.
Instructiones:
Resume as short as you can my obligations. Dont forget numbers, money.
Use "|" to separate the obligations, follow the next format.
Format(Spanish):obligation|obligation|obligation
"""

def ask_to_chatgpt(prompt):
    # Set up your OpenAI API key
    openai.api_key = os.environ["OPENAI_API_KEY"]

    model_engine = "text-davinci-003"
    max_tokens = 1024

    # Call the OpenAI API to generate a response to the prompt
    response = openai.Completion.create(
        engine=model_engine,
        prompt=indications + prompt,
        max_tokens=max_tokens
    )

    # Print the generated response
    return response.choices[0].text
