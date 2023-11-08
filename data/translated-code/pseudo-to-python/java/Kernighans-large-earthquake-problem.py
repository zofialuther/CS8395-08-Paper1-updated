from java.io import BufferedReader, FileReader

class KernighansLargeEarthquakeProblem:
    def main(self):
        try:
            reader = BufferedReader(FileReader("data.txt"))
            inLine = reader.readLine()
            while inLine is not None:
                split = inLine.split()
                magnitude = float(split[2])
                if magnitude > 6:
                    print(inLine)
                inLine = reader.readLine()
        finally:
            if reader:
                reader.close()