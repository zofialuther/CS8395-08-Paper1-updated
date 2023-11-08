class ScriptName:
    def main(args):
        program = System.getProperty("sun.java.command").split(" ")[0]
        print("Program: " + program)