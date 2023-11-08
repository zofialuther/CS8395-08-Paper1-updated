class Patient:
    def __init__(self, id, last_name):
        self.id = id
        self.last_name = last_name
        self.visits = []

class Visit:
    def __init__(self, patient_id, visit_date, score):
        self.patient_id = patient_id
        self.visit_date = visit_date
        self.score = score

def merge_and_aggregate(patients, visits):
    patients.sort(key=lambda x: x.id)
    
    print("Patient ID | Last Name | Last Visit Date | Score Sum | Score Average")
    
    for patient in patients:
        last_visit_date = max(visit.visit_date for visit in patient.visits)
        score_sum = sum(visit.score for visit in patient.visits)
        score_average = score_sum / len(patient.visits)
        
        print(f"{patient.id} | {patient.last_name} | {last_visit_date} | {score_sum} | {score_average}")