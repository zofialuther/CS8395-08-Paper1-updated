from Data.Maybe import fromMaybe
from Data.List import find, isPrefixOf
from Data.Char import toUpper, isUpper

def isAbbreviationOf(abbreviation, command):
    normalizedAbbreviation = abbreviation.upper()
    normalizedCommand = command.upper()
    minimumPrefix = ''.join(takewhile(isUpper, command))
    return minimumPrefix.isPrefixOf(normalizedAbbreviation) and normalizedAbbreviation.isPrefixOf(normalizedCommand)

def expandAbbreviation(commandTable, abbreviation):
    words_list = commandTable.split()
    command = find(lambda x: isAbbreviationOf(abbreviation, x), words_list)
    if command:
        return command.upper()
    else:
        return None

commandTable = "Add ALTer  BAckup Bottom  CAppend Change SCHANGE  CInsert CLAst COMPress COpy " \
                "COUnt COVerlay CURsor DELete CDelete Down DUPlicate Xedit EXPand EXTract Find " \
                "NFind NFINDUp NFUp CFind FINdup FUp FOrward GET Help HEXType Input POWerinput " \
                "Join SPlit SPLTJOIN  LOAD  Locate CLocate  LOWercase UPPercase  LPrefix MACRO " \
                "MErge MODify MOve MSG Next Overlay PARSE PREServe PURge PUT PUTD  Query  QUIT " \
                "READ  RECover REFRESH RENum REPeat  Replace CReplace  RESet  RESTore  RGTLEFT " \
                "RIght LEft  SAVE  SET SHift SI  SORT  SOS  STAck STATus  TOP TRAnsfer Type Up"

def main():
    input_str = input()
    abbreviations = input_str.split()
    results = [fromMaybe("*error*", expandAbbreviation(commandTable, abbr)) for abbr in abbreviations]
    print(' '.join(results))

main()