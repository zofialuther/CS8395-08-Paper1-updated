class S:
    def main(self, arr):
        s = "Declare a class S\nInside the class, declare a main method that takes an array of strings as input\nInside the main method, declare a string variable s and initialize it with the code for the class S\nDeclare a char variable c and initialize it with the value 34 (double quote character)\nPrint the substring of the string s from index 0 to 52, followed by the char c, then again followed by char c, and finally the substring of s from index 52 onwards\nEnd the main method\nEnd the class S"
        c = chr(34)
        print(s[:53] + c + c + s[53:])
        
#End of the class S