from java.nio.file import Files, Paths
from java.nio.charset import Charset
from java.util import List

class ReadAll:
  
    @staticmethod
    def readAllLines(filename):
        file = Paths.get(filename)
        return Files.readAllLines(file, Charset.defaultCharset())
    
    @staticmethod
    def readAllBytes(filename):
        file = Paths.get(filename)
        return Files.readAllBytes(file)