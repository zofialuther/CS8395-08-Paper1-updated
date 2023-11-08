import os

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
    length_stats = {subdir: [] for subdir in translation_subdirs}
    
    for subdir in translation_subdirs:
        translation_dir = os.path.join(base_translation_dir, subdir)
        for root, _, files in os.walk(translation_dir):
            for file in files:
                if file.endswith('.py'):  # Only check .py files
                    file_path = os.path.join(root, file)
                    lines = count_lines(file_path)
                    length_stats[subdir].append(lines)
    
    return length_stats

# Calculate and print the average length for each type of translation
length_stats = calculate_average_length()
for subdir, lines_list in length_stats.items():
    if lines_list:
        average_length = sum(lines_list) / len(lines_list)
        print(f"Average length for {subdir}: {average_length:.2f} LOC")
    else:
        print(f"No files found for {subdir}")

# Run the function
calculate_average_length()
