```python
class AbbreviationsEasy:
    input = None
    COMMAND_TABLE = ""

    def main(self):
        cmdTableArr = self.COMMAND_TABLE.split()
        cmd_table = {}
        for cmd in cmdTableArr:
            cmd_table[cmd] = self.countCaps(cmd)
        userInput = input("Enter command to verify: ")
        user_input = userInput.split()
        for s in user_input:
            match = False
            for cmd, num_caps in cmd_table.items():
                if len(s) >= num_caps and len(s) <= len(cmd):
                    if cmd.upper() == s:
                        print(cmd)
                        match = True
            if not match:
                print("*error*")

    @staticmethod
    def countCaps(word):
        numCaps = 0
        for char in word:
            if char.isupper():
                numCaps += 1
        return numCaps
```