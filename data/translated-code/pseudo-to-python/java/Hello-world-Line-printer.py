from java.io import FileWriter, IOException

class LinePrinter:
    def main(self):
        try:
            lp0 = FileWriter("/dev/lp0")
            lp0.write("Hello World!")
            lp0.close()
        except IOException as e:
            e.printStackTrace()