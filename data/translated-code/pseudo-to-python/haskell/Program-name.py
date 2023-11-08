import System

def main() -> IO():
    getProgName() >>= putStrLn("Program: " + getProgName)