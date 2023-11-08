input_string = "Hello,How,Are,You,Today"
split_by = ","
empty_replace = ""
split = input_string.split(split_by)
period_separated = ".".join(split)
print(period_separated)