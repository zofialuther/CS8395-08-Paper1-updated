import csv

def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def combine_data(patients, visits):
    combined_data = []
    for patient in patients:
        for visit in visits:
            if patient[0] == visit[0]:
                combined_data.append(patient + visit[1:])
    return combined_data

def calculate_sum(scores):
    return sum(map(int, scores))

def calculate_average(scores):
    return sum(map(int, scores)) / len(scores)

def format_data(data):
    transposed_data = list(map(list, zip(*data)))
    max_widths = [max(len(str(item)) for item in column) for column in transposed_data]
    formatted_data = []
    for row in data:
        formatted_row = [str(item).ljust(max_widths[i]) for i, item in enumerate(row)]
        formatted_data.append(' | '.join(formatted_row))
    return formatted_data

patients = read_csv("patients.csv")
visits = read_csv("visits.csv")
combined_data = combine_data(patients, visits)

tabulated_data = [["Patient ID", "Last Name", "Visit Date", "Sum of Scores", "Average Score"]] + combined_data
formatted_tabulated_data = format_data(tabulated_data)

for row in formatted_tabulated_data:
    print(row)