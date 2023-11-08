```python
class WordWrap:
    def __init__(self, text):
        self.text = text
    
    def wrap_text(self, line_width=80):
        # wrap text with default line width or custom line width
        # using StringTokenizer to split the input text into words
        # and format them to fit within the specified line width

if __name__ == "__main__":
    # demonstrate usage of the WordWrap class
    # wrap a long passage of text with both default and custom line width
    passage = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer euismod, urna eget tincidunt tincidunt, nulla felis tempus justo, id tincidunt elit metus nec neque."
    wrapper = WordWrap(passage)
    wrapper.wrap_text()  # wrap with default line width
    wrapper.wrap_text(60)  # wrap with custom line width
```