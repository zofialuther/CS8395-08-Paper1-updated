command_table_text = """
Add ALTer  BAckup Bottom  CAppend Change SCHANGE  CInsert CLAst COMPress COpy
COUnt COVerlay CURsor DELete CDelete Down DUPlicate Xedit EXPand EXTract Find
NFind NFINDUp NFUp CFind FINdup FUp FOrward GET Help HEXType Input POWerinput
Join SPlit SPLTJOIN  LOAD  Locate CLocate  LOWercase UPPercase LPrefix MACRO
MErge MODify MOve MSG Next Overlay PARSE PREServe PURge PUT PUTD  Query  QUIT
READ  RECover REFRESH RENum REPeat  Replace CReplace  RESet  RESTore  RGTLEFT
RIght LEft  SAVE  SET SHift SI  SORT  SOS  STAck STATus  TOP TRAnsfer Type Up
"""

user_words = "riG   rePEAT copies  put mo   rest    types   fup.    6       poweRin"

def find_abbreviations_length(command_table_text):
    command_table = {}
    for word in command_table_text.split():
        abbreviation_length = sum(1 for c in word if c.isupper())
        if abbreviation_length == 0:
            abbreviation_length = len(word)
        command_table[word] = abbreviation_length
    return command_table

def find_abbreviations(command_table):
    abbreviations = {}
    for command, abbreviation_length in command_table.items():
        for length in range(abbreviation_length, len(command)+1):
            abbreviation = command[:length].lower()
            abbreviations[abbreviation] = command.upper()
    return abbreviations

def parse_user_string(user_string, abbreviations):
    user_words = user_string.lower().split()
    commands = []
    for word in user_words:
        if word in abbreviations:
            commands.append(abbreviations[word])
        else:
            commands.append("*error*")
    return ' '.join(commands)

command_table = find_abbreviations_length(command_table_text)
abbreviations_table = find_abbreviations(command_table)
full_words = parse_user_string(user_words, abbreviations_table)

print("user words:", user_words)
print("full words:", full_words)