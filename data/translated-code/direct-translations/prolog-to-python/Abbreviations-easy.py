from typing import List

def validate(word: str, commands: List[str], result: str) -> str:
    if not word:
        return ""
    for command in commands:
        prefix = command[:-len(command) // 2]
        suffix = command[-len(command) // 2:]
        prefix = prefix.upper()
        suffix = suffix.lower()
        word_lower = word.lower()
        prefix_lower = prefix.lower()
        if word_lower.startswith(prefix_lower) and word_lower.endswith(suffix):
            return command.upper()
    return "*error*"

def main() -> None:
    import sys
    args = sys.argv[1:]
    table = "Add ALTer  BAckup Bottom  CAppend Change SCHANGE  CInsert CLAst COMPress COpy COUnt COVerlay CURsor DELete CDelete Down DUPlicate Xedit EXPand EXTract Find NFind NFINDUp NFUp CFind FINdup FUp FOrward GET Help HEXType Input POWerinput Join SPlit SPLTJOIN  LOAD  Locate CLocate  LOWercase UPPercase  LPrefix MACRO MErge MODify MOve MSG Next Overlay PARSE PREServe PURge PUT PUTD  Query  QUIT READ  RECover REFRESH RENum REPeat  Replace CReplace  RESet  RESTore  RGTLEFT RIght LEft  SAVE  SET SHift SI  SORT  SOS  STAck STATus  TOP TRAnsfer Type Up"
    commands = table.split()
    for arg in args:
        result = validate(arg, commands, "")
        print(result, end=" ")
    print()

if __name__ == "__main__":
    main()