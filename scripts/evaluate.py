from calculate_length import *
from calculate_bleu import *
from calculate_syntax import *
import json

if __name__ == "__main__":
    length_dict = report_length()
    syntax_dict = report_syntax()
    bleu_dict = report_bleu()

    data = {'output' : 0,
            'length' : length_dict,
            'syntax' : syntax_dict,
            'bleu' : bleu_dict
            }
    
    
    with open('../output.json', "w") as file:
        json.dump(data, file, indent=4)
