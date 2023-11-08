from typing import List
from dataclasses import dataclass
from datetime import date

@dataclass
class Patient:
    patientID: str
    lastName: str

@dataclass
class Visit:
    visitID: str
    visitDate: str
    score: float

def main():
    patients = [
        Patient("1001", "Hopper"),
        Patient("4004", "Wirth"),
        Patient("3003", "Kemeny"),
        Patient("2002", "Gosling"),
        Patient("5005", "Kurtz")
    ]

    visits = [
        Visit("2002", "2020-09-10", 6.8),
        Visit("1001", "2020-09-17", 5.5),
        Visit("4004", "2020-09-24", 8.4),
        Visit("2002", "2020-10-08", None),
        Visit("1001", ""          , 6.6),
        Visit("3003", "2020-11-12", None),
        Visit("4004", "2020-11-05", 7.0),
        Visit("1001", "2020-11-19", 5.3)
    ]

    patients.sort(key=lambda x: x.patientID)

    print("| PATIENT_ID | LASTNAME | LAST_VISIT | SCORE_SUM | SCORE_AVG |")
    for patient in patients:
        patientVisits = [v for v in visits if v.visitID == patient.patientID]
        lastVisit = max([v.visitDate for v in patientVisits], default="   None   ")
        scoreSum = sum([v.score for v in patientVisits if v.score is not None])
        scoreAverage = sum([v.score for v in patientVisits if v.score is not None]) / len([v for v in patientVisits if v.score is not None])
        patientDetails = f"{patient.patientID:12}{patient.lastName:11}{lastVisit:13}{scoreSum:12.2f}{scoreAverage:12.2f}"
        print(patientDetails)

if __name__ == "__main__":
    main()