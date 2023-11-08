import textwrap

def fill_paragraph(text, width=70):
    return textwrap.fill(text, width)

txt = '''\
Reformat the single paragraph in 'text' to fit in lines of no more
than 'width' columns, and return a new string containing the entire
wrapped paragraph.  As with wrap(), tabs are expanded and other
whitespace characters converted to space.  See TextWrapper class for
available keyword args to customize wrapping behaviour.'''

print(fill_paragraph(txt, width=75))
print(fill_paragraph(txt, width=45))
print(fill_paragraph(txt, width=85))