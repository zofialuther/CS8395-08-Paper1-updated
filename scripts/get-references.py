import os
import shutil

# Define the source and destination directory paths
source_dir = '../../RosettaCodeData/Task'  # TODO: Update this to your RosettaCodeData/Task path
destination_dir = '../../CS8395-08-Paper1-updated/data/reference-samples'  # TODO: Update this to your new directory structure path

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
            python_path = os.path.join(task_path, 'python')
            dest_task_path = os.path.join(destination_dir, task, 'python')
            os.makedirs(dest_task_path, exist_ok=True)  # Create the destination path

            # Copy each Python file to the new location
            for file in os.listdir(python_path):
                if file.endswith('.py'):  # Ensure it's a Python file
                    src_file_path = os.path.join(python_path, file)
                    dest_file_path = os.path.join(dest_task_path, file)
                    shutil.copy2(src_file_path, dest_file_path)  # copy2 preserves metadata


# Call the function to start the copying process
copy_files()
