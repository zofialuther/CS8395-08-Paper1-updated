import os
import requests
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from tqdm import tqdm

# Define the source directory path and the base destination directory path
source_dir = '../../CS8395-08-Paper1-updated/data/source-code'  # Replace with your source code directory path
intermediate_rep_dir = '../../CS8395-08-Paper1-updated/data/intermediate-rep'  # Replace with your intermediate rep directory path

api_key = os.environ['OPENAI_API_KEY']

# Function to generate pseudocode using the GPT model
def generate_pseudocode(source_code, llm):
    # Prepare the prompt for the language model
    prompt = f"Generate a meaningful description for the following code:\n\n{source_code}\n\n"
    output = llm.predict(prompt)
    return output

# Function to iterate over the source files and generate pseudocode
def generate_pseudocode_for_all(llm):
    pseudocode_dir = os.path.join(intermediate_rep_dir, 'descriptions')
    os.makedirs(pseudocode_dir, exist_ok=True)  # Create 'pseudocode' directory if it doesn't exist

    for language_dir in os.listdir(source_dir):
        language_path = os.path.join(source_dir, language_dir)
        if not os.path.isdir(language_path):
            continue  # Skip files, only interested in directories

        language_pseudocode_dir = os.path.join(pseudocode_dir, language_dir)
        os.makedirs(language_pseudocode_dir, exist_ok=True)  # Create language-specific pseudocode directory

        for task_dir in tqdm(os.listdir(language_path)):
            task_path = os.path.join(language_path, task_dir)
            if not os.path.isdir(task_path):
                continue  # Skip files, only interested in directories

            task_files = os.listdir(task_path)
            if task_files:  # If there are files in the task folder
                source_file_path = os.path.join(task_path, task_files[0])  # Taking the first file
                with open(source_file_path, 'r') as source_file:
                    source_code = source_file.read()

                # Generate pseudocode from the source code
                pseudocode = generate_pseudocode(source_code, llm)

                # Define the path for the pseudocode file
                pseudocode_file_path = os.path.join(language_pseudocode_dir, f"{task_dir}.txt")

                with open(pseudocode_file_path, 'w') as pseudocode_file:
                    pseudocode_file.write(pseudocode)

# Run the pseudocode generation process
llm = ChatOpenAI(model='gpt-3.5-turbo-1106')
generate_pseudocode_for_all(llm)
