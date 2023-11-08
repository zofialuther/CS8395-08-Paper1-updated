```python
def strip_block_comments(input_string):
    # Set Prolog flag to use double quotes as codes
    prolog_code_flag = True
    
    # Main predicate to process input and remove block comments
    def strip_block_comments_helper(input_string):
        # DCG rules to recognize and remove block comments
        # Recursive call to strip_block_comments_helper if block comment is found
        
    # Format output within triple backticks for Markdown use
    output = "```" + strip_block_comments_helper(input_string) + "```"
    return output
```