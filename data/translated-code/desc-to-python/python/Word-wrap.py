import textwrap

# Input text
input_text = "This is a sample paragraph that needs to be wrapped to fit within a specified width using textwrap module in Python."

# Wrap text to fit within specified width
wrapped_text = textwrap.fill(input_text, width=30)

print(wrapped_text)  # Output: This is a sample paragraph
                      #         that needs to be wrapped
                      #         to fit within a specified
                      #         width using textwrap
                      #         module in Python.