from typing import List
from dataclasses import dataclass

@dataclass
class Patient:
    patientID: int
    lastName: str

@dataclass
class Visit:
    visitID: int
    visitDate: str
    score: int

class MergeAndAggregateDatasets:
    @staticmethod
    def main():
        patients = [Patient(1, 'Smith'), Patient(2, 'Johnson'), Patient(3, 'Williams')]
        visits = [Visit(1, '2022-01-01', 90), Visit(2, '2022-01-15', 85), Visit(3, '2022-02-01', 95)]
        
        patients.sort(key=lambda x: x.patientID)
        print("PatientID | Last Name | Last Visit Date | Score Sum | Score Average")
        
        for patient in patients:
            patient_visits = [visit for visit in visits if visit.visitID == patient.patientID]
            last_visit_date = max(patient_visits, key=lambda x: x.visitDate).visitDate
            score_sum = sum(visit.score for visit in patient_visits)
            score_average = score_sum / len(patient_visits)
            print(f"{patient.patientID} | {patient.lastName} | {last_visit_date} | {score_sum} | {score_average}")