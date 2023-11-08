import sys

def main():
    args = sys.argv
    table = command_table()
    commands = table.split(" \t\n")
    for arg in args:
        word = str(arg)
        result = validate(word, commands)
        print(result, end=" ")
    print("\n")

def validate(word, commands):
    for command in commands:
        prefix, suffix = command[:len(command)//2], command[len(command)//2:]
        prefix = prefix.upper()
        suffix = suffix.lower()
        low_word = word.lower()
        low_prefix = prefix.lower()
        if low_word.startswith(low_prefix) and low_word in command.lower():
            return command.upper()

def command_table():
    return "Add ALTer BAckup Bottom CAppend Change SCHANGE CInsert CLAst COMPress COpy COUnt COVerlay CURsor DELete CDelete Down DUPlicate Xedit EXPand EXTract Find NFind NFINDUp NFUp CFind FINdup FUp FOrward GET Help HEXType Input POWerinput Join SPlit SPLTJOIN LOAD Locate CLocate LOWercase UPPercase LPrefix MACRO MErge MODify MOve MSG Next Overlay PARSE PREServe PURge PUT PUTD Query QUIT READ RECover REFRESH RENum REPeat Replace CReplace RESet RESTore RGTLEFT RIght LEft SAVE SET SHift SI SORT SOS STAck STATus TOP TRAnsfer Type Up"

if __name__ == "__main__":
    main()