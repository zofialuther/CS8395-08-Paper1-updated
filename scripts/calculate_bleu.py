import os
from collections import defaultdict
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction
from tqdm import tqdm

# Define the directories
reference_dir = '../../CS8395-08-Paper1-updated/data/reference-samples'  # Path to the directory with reference Python files
translation_dirs = {
    'direct': '../../CS8395-08-Paper1-updated/data/translated-code/direct-translations',
    'pseudo': '../../CS8395-08-Paper1-updated/data/translated-code/pseudo-to-python',
    'desc': '../../CS8395-08-Paper1-updated/data/translated-code/desc-to-python'
}

# Function to read and tokenize a file
def read_and_tokenize(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().split()

# Load the reference translations
references = {}
for task in tqdm(os.listdir(reference_dir), desc='Loading reference translations'):
    task_path = os.path.join(reference_dir, task)
    if os.path.isdir(task_path):
        # Assume there is a subdirectory named 'python' that contains the reference files
        python_ref_dir = os.path.join(task_path, 'python')
        if os.path.isdir(python_ref_dir):
            references[task] = [read_and_tokenize(os.path.join(python_ref_dir, ref_file))
                                for ref_file in os.listdir(python_ref_dir) if ref_file.endswith('.py')]

# Load the translated files and calculate BLEU scores
bleu_scores = defaultdict(lambda: defaultdict(list))
for trans_type, trans_dir in translation_dirs.items():
    print(f"Processing {trans_type} translations:")
    for language in tqdm(os.listdir(trans_dir), desc=f'Processing languages for {trans_type}'):
        language_path = os.path.join(trans_dir, language)
        if os.path.isdir(language_path):
            for trans_file in os.listdir(language_path):
                problem_name, _ = os.path.splitext(trans_file)
                if problem_name in references:
                    trans_file_path = os.path.join(language_path, trans_file)
                    candidate = read_and_tokenize(trans_file_path)
                    try:
                        score = corpus_bleu([references[problem_name]], [candidate],
                                            smoothing_function=SmoothingFunction().method1)
                        bleu_scores[trans_type][language].append(score)
                    except AssertionError as e:
                        print(f"AssertionError: {e}")
                        print(f"Task causing error: {problem_name}")
                        print(f"Number of reference translations for this task: {len(references[problem_name])}")
                        print(f"References for task {problem_name}: {references[problem_name]}")
                        print(f"Candidate translation for task {problem_name}: {candidate}")
                        continue

# Compute the average BLEU scores for each translation type and language
def report_bleu():
    average_bleu_scores = defaultdict(dict)
    cumulative_bleu_scores = defaultdict(list)
    report_dict = {}
    for trans_type, languages in bleu_scores.items():
        subdir_dict = {}
        print(f"Average BLEU score for {trans_type} translations:")
        for language, scores in languages.items():
            if scores:
                avg_score = sum(scores) / len(scores)
                average_bleu_scores[trans_type][language] = avg_score
                cumulative_bleu_scores[trans_type].extend(scores)  # For cumulative average
                print(f"  {language}: {avg_score:.4f}")
                subdir_dict[language] = avg_score
        # Calculate the cumulative average BLEU score for the translation type
        if cumulative_bleu_scores[trans_type]:
            cumul_avg_score = sum(cumulative_bleu_scores[trans_type]) / len(cumulative_bleu_scores[trans_type])
            print(f"  Cumulative average: {cumul_avg_score:.4f}\n")
            subdir_dict['Cumulative average'] = cumul_avg_score

        report_dict[f'Average BLEU score for {trans_type}'] = subdir_dict

    return report_dict
    
if __name__ == "__main__":
    report_bleu()
