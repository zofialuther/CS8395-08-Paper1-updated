import os
from collections import defaultdict

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
    syntax_results = defaultdict(lambda: defaultdict(lambda: {'valid': 0, 'invalid': 0}))
    cumulative_results = defaultdict(lambda: {'valid': 0, 'invalid': 0})
    
    for subdir in translation_subdirs:
        translation_dir = os.path.join(base_translation_dir, subdir)
        for root, dirs, files in os.walk(translation_dir):
            language = os.path.basename(root)  # Get the language from the directory name
            for file in files:
                if file.endswith('.py'):  # Only check .py files
                    file_path = os.path.join(root, file)
                    is_valid = check_syntax(file_path)
                    syntax_category = 'valid' if is_valid else 'invalid'
                    syntax_results[subdir][language][syntax_category] += 1
                    cumulative_results[subdir][syntax_category] += 1
    
    return syntax_results, cumulative_results

# Calculate and print the syntax accuracy for each type of translation by language and the cumulative average
def report_syntax():
    syntax_results, cumulative_results = check_translations_syntax()
    report_dict = {}
    for subdir, languages in syntax_results.items():
        subdir_dict = {}
        print(f"Syntax accuracy for {subdir}:")
        for language, counts in languages.items():
            total = counts['valid'] + counts['invalid']
            if total > 0:
                accuracy = counts['valid'] / total
                print(f"  {language}: {accuracy:.4f} ({counts['valid']} valid out of {total})")
                subdir_dict[language] = accuracy
        # Calculate the cumulative syntax accuracy for the translation type
        cumul_counts = cumulative_results[subdir]
        cumul_total = cumul_counts['valid'] + cumul_counts['invalid']
        if cumul_total > 0:
            cumul_accuracy = cumul_counts['valid'] / cumul_total
            print(f"  Cumulative: {cumul_accuracy:.4f} ({cumul_counts['valid']} valid out of {cumul_total})\n")
            subdir_dict['Cumulative average'] = cumul_accuracy

        report_dict[f'Average syntactical accuracy for {subdir}'] = subdir_dict

    return report_dict

if __name__ == "__main__":
    report_syntax()
