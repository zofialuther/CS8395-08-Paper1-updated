from java.util.function import IntSupplier
from java.util.stream import IntStream

class ValueCapture:
    @staticmethod
    def main(args):
        closures = (IntStream.rangeClosed(0, 10)
                    .map(lambda x: IntSupplier(lambda: x*x))
                    .collect(Collectors.toList()))
        
        closure = closures[3]
        print(closure.getAsInt())