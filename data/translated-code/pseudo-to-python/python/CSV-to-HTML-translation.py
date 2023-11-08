```python
from prettytable import PrettyTable

table = PrettyTable(border=1, header=False, hrules=0, vrules=0, field_names=["Character", "Speech"])
table.title = "csv2html extra program output"

table.field_names = ["Character", "Speech"]
table.add_row(["The multitude", "The messiah! Show us the messiah!"])
table.add_row(["Brians mother", "<angry>Now you listen here! He's not the messiah; he's a very naughty boy! Now go away!</angry>"])
table.add_row(["The multitude", "Who are you?"])
table.add_row(["Brians mother", "I'm his mother; that's who!"])
table.add_row(["The multitude", "Behold his mother! Behold his mother!"])

print(table)
```