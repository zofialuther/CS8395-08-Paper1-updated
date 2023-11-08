from typing import List

def isAbbreviationOf(abbreviation: str, command: str) -> bool:
    normalizedAbbreviation = abbreviation.upper()
    normalizedCommand = command.upper()
    minimumPrefix = "".join([c for c in normalizedCommand if c.isupper()])
    return minimumPrefix in normalizedAbbreviation and normalizedAbbreviation.startswith(minimumPrefix)

def expandAbbreviation(commandTable: str, abbreviation: str) -> str:
    wordsList = commandTable.split()
    for word in wordsList:
        if isAbbreviationOf(abbreviation, word):
            return word.upper()
    return ""

commandTable = "Add ALTer  BAckup Bottom  CAppend Change SCHANGE  CInsert CLAst COMPress COpy" + \
    "COUnt COVerlay CURsor DELete CDelete Down DUPlicate Xedit EXPand EXTract Find" + \
    "NFind NFINDUp NFUp CFind FINdup FUp FOrward GET Help HEXType Input POWerinput" + \
    "Join SPlit SPLTJOIN  LOAD  Locate CLocate  LOWercase UPPercase  LPrefix MACRO" + \
    "MErge MODify MOve MSG Next Overlay PARSE PREServe PURge PUT PUTD  Query  QUIT" + \
    "READ  RECover REFRESH RENum REPeat  Replace CReplace  RESet  RESTore  RGTLEFT" + \
    "RIght LEft  SAVE  SET SHift SI  SORT  SOS  STAck STATus  TOP TRAnsfer Type Up"

def main():
    inputStr = input("Enter the abbreviations: ")
    abbreviations = inputStr.split()
    results = [expandAbbreviation(commandTable, abbr) for abbr in abbreviations]
    print(" ".join(results))

if __name__ == "__main__":
    main()