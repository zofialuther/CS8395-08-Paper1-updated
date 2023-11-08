import os
from collections import defaultdict

# Define the base directory where all translations are stored
base_translation_dir = '../../CS8395-08-Paper1-updated/data/translated-code'  # Replace with your actual path

# Define the translation subdirectories
translation_subdirs = ['direct-translations', 'pseudo-to-python', 'desc-to-python']

# Function to count the lines of a file
def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for line in file)

# Function to iterate over the files and count their lines
def calculate_average_length():
    length_stats = defaultdict(lambda: defaultdict(list))  # Nested defaultdict for organizing by subdir and language
    
    for subdir in translation_subdirs:
        translation_dir = os.path.join(base_translation_dir, subdir)
        for root, dirs, files in os.walk(translation_dir):
            # The language should be the name of the subdirectory within the translation type directory
            language = os.path.basename(root)
            for file in files:
                if file.endswith('.py'):  # Only check .py files
                    file_path = os.path.join(root, file)
                    lines = count_lines(file_path)
                    length_stats[subdir][language].append(lines)
    
    return length_stats

# Calculate and print the average length for each type of translation by language and the cumulative average
def report_length():
    length_stats = calculate_average_length()
    for subdir, languages in length_stats.items():
        print(f"Average length for {subdir}:")
        all_lengths = []  # List to keep track of all lengths for cumulative average
        for language, lines_list in languages.items():
            if lines_list:
                average_length = sum(lines_list) / len(lines_list)
                all_lengths.extend(lines_list)  # Add all lengths to the cumulative list
                print(f"  {language}: {average_length:.2f} LOC")
            else:
                print(f"  No files found for {language}")
        # Calculate the cumulative average length for the translation type
        if all_lengths:
            cumulative_average_length = sum(all_lengths) / len(all_lengths)
            print(f"  Cumulative average: {cumulative_average_length:.2f} LOC\n")
        else:
            print("  No files found for cumulative average\n")

if __name__ == "__main__":
    report_length()
