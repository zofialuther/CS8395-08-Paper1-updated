class ScriptName:
    @staticmethod
    def main(args: str):
        program = System.getProperty("sun.java.command").split(" ")[0]
        print(program)