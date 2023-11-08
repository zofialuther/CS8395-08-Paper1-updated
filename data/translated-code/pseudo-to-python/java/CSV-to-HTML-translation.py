```python
def escapeChars(lineIn):
    sb = ""
    lineLength = len(lineIn)
    for i in range(lineLength):
        c = lineIn[i]
        if c == '"':
            sb += "&quot;"
        elif c == '&':
            sb += "&amp;"
        elif c == '\'':
            sb += "&apos;"
        elif c == '<':
            sb += "&lt;"
        elif c == '>':
            sb += "&gt;"
        else:
            sb += c
    return sb

def tableHeader(ps, columns):
    ps.print("<tr>")
    for i in range(len(columns)):
        ps.print("<th>")
        ps.print(columns[i])
        ps.print("</th>")
    ps.println("</tr>")

def tableRow(ps, columns):
    ps.print("<tr>")
    for i in range(len(columns)):
        ps.print("<td>")
        ps.print(columns[i])
        ps.print("</td>")
    ps.println("</tr>")

def main(args):
    withTableHeader = (len(args) != 0)
    stdout = sys.stdout

    stdout.println("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">")
    stdout.println("<html xmlns=\"http://www.w3.org/1999/xhtml\">")
    stdout.println("<head><meta http-equiv=\"Content-type\" content=\"text/html;charset=UTF-8\"/>")
    stdout.println("<title>Csv2Html</title>")
    stdout.println("<style type=\"text/css\">")
    stdout.println("body{background-color:#FFF;color:#000;font-family:OpenSans,sans-serif;font-size:10px;}")
    stdout.println("table{border:0.2em solid #2F6FAB;border-collapse:collapse;}")
    stdout.println("th{border:0.15em solid #2F6FAB;padding:0.5em;background-color:#E9E9E9;}")
    stdout.println("td{border:0.1em solid #2F6FAB;padding:0.5em;background-color:#F9F9F9;}</style>")
    stdout.println("</head><body><h1>Csv2Html</h1>")
    stdout.println("<table>")
    firstLine = True
    while True:
        stdinLine = br.readLine()
        if stdinLine is None:
            break
        columns = escapeChars(stdinLine).split(",")
        if withTableHeader == True and firstLine == True:
            tableHeader(stdout, columns)
            firstLine = False
        else:
            tableRow(stdout, columns)
    stdout.println("</table></body></html>")
```