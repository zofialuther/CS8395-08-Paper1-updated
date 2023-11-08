from ctypes import CDLL

# Load the native library
lib = CDLL("JNIDemo")

# Define the JNIDemo class
class JNIDemo:
    # Define the callStrdup method as a native method
    callStrdup = lib.callStrdup

    # Define the main method
    def main(self, args):
        # Print the result of calling the callStrdup method with "Hello World!" as the argument
        print(self.callStrdup("Hello World!"))