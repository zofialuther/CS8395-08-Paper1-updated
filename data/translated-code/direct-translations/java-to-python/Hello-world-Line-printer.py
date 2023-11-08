from io import open

class LinePrinter:
    def main(self, args):
        try:
            with open('/dev/lp0', 'w') as lp0:
                lp0.write("Hello World!")
        except IOError as ioe:
            print(ioe)