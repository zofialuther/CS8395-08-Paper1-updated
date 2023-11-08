def theader(header_data):
    header = "<tr>"
    for item in header_data:
        header += "<th>" + item + "</th>"
    header += "</tr>"
    return header

def trow(row_data):
    row = "<tr>"
    for item in row_data:
        row += "<td>" + item + "</td>"
    row += "</tr>"
    return row

def trows(rows_data):
    rows = ""
    for row in rows_data:
        rows += trow(row)
    return rows

def table(header_data, rows_data):
    table = "<table>"
    table += theader(header_data)
    table += trows(rows_data)
    table += "</table>"
    return table

def print_html(html):
    print(html)

header = ["Name", "Age", "Gender"]
rows = [["John", "25", "Male"], ["Jane", "30", "Female"], ["Bob", "22", "Male"]]

html_table = table(header, rows)
print_html(html_table)