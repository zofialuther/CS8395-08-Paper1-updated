from prettytable import PrettyTable

# 1. Initialize a table with a header and body
table = PrettyTable(['Character', 'Speech'])

# 2. Create a row in the table for each character and their speech
table.add_row(['Character1', 'Speech1'])
table.add_row(['Character2', 'Speech2'])
table.add_row(['Character3', 'Speech3'])

# 3. Set the style for each cell in the table with the specified color, background, border, and padding
table.set_style({'color': 'blue', 'background': 'white', 'border': True, 'padding_width': 1})

# 4. Populate the table with the characters and their respective speeches
# (Already done in step 2)

# 5. Display the table on the webpage
print(table)