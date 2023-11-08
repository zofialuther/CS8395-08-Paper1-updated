import os
import shutil

# Define the source and destination directory paths
source_dir = '../../RosettaCodeData/Task'  # TODO: Update this to your RosettaCodeData/Task path
destination_dir = '../../CS8395-08-Paper1-updated/data/'  # TODO: Update this to your new directory structure path

# Define the required languages
required_languages = {'Python', 'Java', 'Prolog', 'Haskell'}

# Function to check if all required language folders exist for a task
def all_languages_present(task_path):
    languages = set(os.listdir(task_path))
    return required_languages.issubset(languages)

# Function to copy the files for tasks that have all required languages
def copy_files():
    for task in os.listdir(source_dir):
        task_path = os.path.join(source_dir, task)
        if os.path.isdir(task_path) and all_languages_present(task_path):
            for language in required_languages:
                language_folder = os.path.join(task_path, language)
                files = [f for f in os.listdir(language_folder) if os.path.isfile(os.path.join(language_folder, f))]
                if files:  # If there are files in the language folder
                    # Select the first file
                    source_file = os.path.join(language_folder, files[0])
                    destination_language_folder = os.path.join(destination_dir, 'source-code', language.lower(), task)
                    os.makedirs(destination_language_folder, exist_ok=True)
                    # Copy the first file to the new structure
                    destination_file = os.path.join(destination_language_folder, files[0])
                    shutil.copy2(source_file, destination_file)

# Call the function to start the copying process
copy_files()
