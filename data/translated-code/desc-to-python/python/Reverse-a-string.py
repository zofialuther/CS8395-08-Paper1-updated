def reverse_and_say(unicode_string):
    converted_string = bytes.fromhex(unicode_string).decode('utf-8')
    reversed_string = converted_string[::-1]
    say_rev(reversed_string)