from easygui import *

class GUI_Interaction:

    def __init__(self):
        self.dialog = None

    def create_dialog(self):
        self.dialog = multenterbox('Rosetta Code', 'GUI_Interaction', ['Value :'], ['',])
        self.dialog.append(buttonbox('Choose action:', choices=['increment', 'random']))

    def set_layout(self):
        pass

    def increment(self, value):
        val = int(value)
        val += 1
        self.dialog[0] = str(val)

    def my_random(self, value):
        choice = buttonbox('Confirm your choice !', 'GUI Interaction', choices=['ok', 'cancel'])
        if choice == 'ok':
            x = randint(0, 10000)
            self.dialog[0] = str(x)

    def input(self, value):
        try:
            int(value)
        except ValueError:
            msgbox('Please enter a number')
            self.dialog[0] = ''

    def open_dialog(self):
        self.create_dialog()
        while True:
            if self.dialog[1] == 'increment':
                self.increment(self.dialog[0])
            elif self.dialog[1] == 'random':
                self.my_random(self.dialog[0])
            self.input(self.dialog[0])
            self.create_dialog()

GUI_Interaction().open_dialog()