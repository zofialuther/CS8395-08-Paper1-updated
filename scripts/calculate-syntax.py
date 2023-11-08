import os

# Define the base directory where all translations are stored
base_translation_dir = '../../CS8395-08-Paper1-updated/data/translated-code'  # Replace with your actual path

# Define the translation subdirectories
translation_subdirs = ['direct-translations', 'pseudo-to-python', 'desc-to-python']

# Function to check if a Python file is syntactically valid
def check_syntax(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        source_code = file.read()
    try:
        compile(source_code, file_path, 'exec')
        return True
    except SyntaxError:
        return False

# Function to iterate over the files and check their syntax
def check_translations_syntax():
    syntax_results = {subdir: {'valid': 0, 'invalid': 0} for subdir in translation_subdirs}
    
    for subdir in translation_subdirs:
        translation_dir = os.path.join(base_translation_dir, subdir)
        for root, _, files in os.walk(translation_dir):
            for file in files:
                if file.endswith('.py'):  # Only check .py files
                    file_path = os.path.join(root, file)
                    is_valid = check_syntax(file_path)
                    if is_valid:
                        syntax_results[subdir]['valid'] += 1
                    else:
                        syntax_results[subdir]['invalid'] += 1
    
    return syntax_results

# Calculate and print the syntax accuracy for each type of translation
syntax_results = check_translations_syntax()
for subdir, counts in syntax_results.items():
    total = counts['valid'] + counts['invalid']
    if total > 0:
        accuracy = counts['valid'] / total
        print(f"Syntax accuracy for {subdir}: {accuracy:.4f} ({counts['valid']} valid out of {total})")
    else:
        print(f"No files to check in {subdir}")

# Run the syntax check
check_translations_syntax()
