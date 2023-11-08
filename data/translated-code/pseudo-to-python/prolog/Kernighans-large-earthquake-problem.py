def process_line(Line):
    split_line(Line, Magnitude_string)
    parse_magnitude(Magnitude_string, Magnitude)
    check_magnitude(Magnitude, Line)

def process_stream(Stream):
    read_line(Stream, String)
    process_line(String)
    process_stream(Stream)

def process_file(File):
    Stream = open(File, 'r')
    process_stream(Stream)
    Stream.close()

def split_line(Line, Magnitude_string):
    split_string(Line, " \s\t", " \s\t", [_, _, Magnitude_string])

def parse_magnitude(Magnitude_string, Magnitude):
    read_term_from_atom(Magnitude_string, Magnitude, [])

def check_magnitude(Magnitude, Line):
    if Magnitude > 6:
        write_line(Line)

def write_line(Line):
    print('%w\n' % Line)