from calculate_length import *
from calculate_bleu import *
from calculate_syntax import *
import json

if __name__ == "__main__":
    report_length()
    report_syntax()
    report_bleu()

    data = {'output' : 0}
    
    
    with open('../output.json', "w") as file:
        json.dump(data, file, indent=4)
