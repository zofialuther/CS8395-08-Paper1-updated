from string import Formatter

class StringBuilder:
    def __init__(self):
        self.data = []

    def append(self, text):
        self.data.append(text)

    def __str__(self):
        return "".join(self.data)

sb = StringBuilder()
formatter = Formatter()
adjective = "little"
sentence = "Mary had a {} lamb".format(adjective)
formatted_sentence = formatter.format(sentence)
sb.append(formatted_sentence)