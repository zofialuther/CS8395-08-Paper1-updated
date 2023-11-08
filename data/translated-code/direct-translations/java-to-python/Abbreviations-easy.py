```python
class AbbreviationsEasy:
    COMMAND_TABLE = "  Add ALTer  BAckup Bottom  CAppend Change SCHANGE  CInsert CLAst COMPress COpy\n" + \
                    " COUnt COVerlay CURsor DELete CDelete Down DUPlicate Xedit EXPand EXTract Find\n" + \
                    " NFind NFINDUp NFUp CFind FINdup FUp FOrward GET Help HEXType Input POWerinput\n" + \
                    " Join SPlit SPLTJOIN  LOAD  Locate CLocate  LOWercase UPPercase  LPrefix MACRO\n" + \
                    " MErge MODify MOve MSG Next Overlay PARSE PREServe PURge PUT PUTD  Query  QUIT\n" + \
                    " READ  RECover REFRESH RENum REPeat  Replace CReplace  RESet  RESTore  RGTLEFT\n" + \
                    " RIght LEft  SAVE  SET SHift SI  SORT  SOS  STAck STATus TOP TRAnsfer Type Up"

    def main(self):
        cmd_table = {}
        cmd_table_arr = AbbreviationsEasy.COMMAND_TABLE.split()

        for word in cmd_table_arr:
            cmd_table[word] = self.count_caps(word)

        user_input = input("Please enter your command to verify: ").split()

        for s in user_input:
            match = False
            for cmd in cmd_table:
                if len(s) >= cmd_table[cmd] and len(s) <= len(cmd):
                    temp = cmd.upper()
                    if temp.startswith(s.upper()):
                        print(temp, end=" ")
                        match = True
            if not match:
                print("*error*", end=" ")

    def count_caps(self, word):
        return sum(1 for c in word if c.isupper())


abb = AbbreviationsEasy()
abb.main()
```