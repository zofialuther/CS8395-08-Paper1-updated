import os
import requests
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from tqdm import tqdm

# Define the source directory path and the base destination directory path
source_dir = '../../CS8395-08-Paper1-updated/data/source-code'
base_destination_dir = '../../CS8395-08-Paper1-updated/data/translated-code'

# Define the API details if using an API-based language model
api_key = os.environ['OPENAI_API_KEY']

# Function to translate code using the GPT model
def translate_code(source_code, target_lang, llm):
    # Prepare the prompt for the language model
    prompt = f"Translate this code to {target_lang}:\n\n{source_code}\n\n"
    output = llm.predict(prompt)
    return output
    

# Function to determine the language based on the directory name
def get_language_from_dir(dirname):
    if dirname == 'java':
        return 'Java'
    elif dirname == 'haskell':
        return 'Haskell'
    elif dirname == 'prolog':
        return 'Prolog'
    else:
        raise ValueError(f"Unexpected directory name: {dirname}")

# Function to iterate over the source files and generate translations
def generate_translations(llm):
    for language_dir in os.listdir(source_dir):
        language_path = os.path.join(source_dir, language_dir)
        if not os.path.isdir(language_path):
            continue  # Skip files, only interested in directories

        for task_dir in tqdm(os.listdir(language_path)):
            task_path = os.path.join(language_path, task_dir)
            if not os.path.isdir(task_path):
                continue  # Skip files, only interested in directories

            task_files = os.listdir(task_path)
            if task_files:  # If there are files in the task folder
                source_file_path = os.path.join(task_path, task_files[0])  # Taking the first file
                with open(source_file_path, 'r') as source_file:
                    source_code = source_file.read()

                # Translate the source code to Python
                translated_code = translate_code(source_code, 'Python', llm)

                # Define the path for the translated file
                target_lang_folder = f"{language_dir}-to-python"
                destination_folder = os.path.join(base_destination_dir, target_lang_folder)
                os.makedirs(destination_folder, exist_ok=True)
                translated_file_path = os.path.join(destination_folder, f"{task_dir}.py")

                with open(translated_file_path, 'w') as translated_file:
                    translated_file.write(translated_code)

# Run the translation generation process
llm = ChatOpenAI(model='gpt-3.5-turbo-1106')
generate_translations(llm)
