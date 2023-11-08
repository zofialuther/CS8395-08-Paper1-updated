import os
import requests
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from tqdm import tqdm

# Define the base directories
description_dir = '../../CS8395-08-Paper1-updated/data/intermediate-rep/descriptions'  # Replace with your pseudocode directory path
translated_code_dir = '../../CS8395-08-Paper1-updated/data/translated-code/desc-to-python'  # Replace with your translated code directory path

api_key = os.environ['OPENAI_API_KEY']


# Function to translate pseudocode to Python using the GPT model
def translate_to_python(description, llm):
    # Prepare the prompt for the language model
    prompt = f"Translate the following description to Python. Don't include anything else in your response other than the Python code. \n\n{description}\n\n"
    output = llm.predict(prompt)
    return output

# Function to iterate over the pseudocode files and generate Python code
def translate_description_to_python(llm):
    for language in os.listdir(description_dir):
        language_path = os.path.join(description_dir, language)
        if not os.path.isdir(language_path):
            continue  # Skip files, only interested in directories

        for description_file in tqdm(os.listdir(language_path)):
            # Define the path for the translated Python code file
            problem_name = os.path.splitext(description_file)[0]  # Remove file extension to get problem name
            python_file_path = os.path.join(translated_code_dir, language, f"{problem_name}.py")

            if not os.path.exists(python_file_path):
                description_path = os.path.join(language_path, description_file)
                with open(description_path, 'r') as file:
                    description = file.read()

                # Translate the pseudocode to Python code
                python_code = translate_to_python(description, llm)

                # Define the path for the translated Python code file
                problem_name = os.path.splitext(description_file)[0]  # Remove file extension to get problem name
                python_file_path = os.path.join(translated_code_dir, language, f"{problem_name}.py")
                os.makedirs(os.path.dirname(python_file_path), exist_ok=True)

                with open(python_file_path, 'w') as file:
                    file.write(python_code)

# Run the translation process
llm = ChatOpenAI(model='gpt-3.5-turbo-1106')
translate_description_to_python(llm)
