import sys

def escapeChars(lineIn):
    sb = ""
    for c in lineIn:
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
    ps.write("<tr>")
    for column in columns:
        ps.write("<th>")
        ps.write(column)
        ps.write("</th>")
    ps.write("</tr>")

def tableRow(ps, columns):
    ps.write("<tr>")
    for column in columns:
        ps.write("<td>")
        ps.write(column)
        ps.write("</td>")
    ps.write("</tr>")

if __name__ == "__main__":
    withTableHeader = (len(sys.argv) != 0)
    
    stdout = sys.stdout
    
    stdout.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">")
    stdout.write("<html xmlns=\"http://www.w3.org/1999/xhtml\">")
    stdout.write("<head><meta http-equiv=\"Content-type\" content=\"text/html;charset=UTF-8\"/>")
    stdout.write("<title>Csv2Html</title>")
    stdout.write("<style type=\"text/css\">")
    stdout.write("body{background-color:#FFF;color:#000;font-family:OpenSans,sans-serif;font-size:10px;}")
    stdout.write("table{border:0.2em solid #2F6FAB;border-collapse:collapse;}")
    stdout.write("th{border:0.15em solid #2F6FAB;padding:0.5em;background-color:#E9E9E9;}")
    stdout.write("td{border:0.1em solid #2F6FAB;padding:0.5em;background-color:#F9F9F9;}</style>")
    stdout.write("</head><body><h1>Csv2Html</h1>")

    stdout.write("<table>")
    firstLine = True
    while True:
        stdinLine = sys.stdin.readline().strip()
        if not stdinLine:
            break
        columns = escapeChars(stdinLine).split(",")
        if withTableHeader and firstLine:
            tableHeader(stdout, columns)
            firstLine = False
        else:
            tableRow(stdout, columns)
    
    stdout.write("</table></body></html>")