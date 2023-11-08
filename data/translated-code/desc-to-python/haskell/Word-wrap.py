```python
ss = "This is a long passage of text that needs to be wrapped to fit within a certain line length."

def wordwrap(text, max_line_length):
    words = text.split()
    lines = []
    current_line = words[0]
    
    for word in words[1:]:
        if len(current_line) + len(word) < max_line_length:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    
    return "\n".join(lines)

def main():
    print(wordwrap(ss, 72))
    print(wordwrap(ss, 32))

main()
```