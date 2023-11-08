from data.text import split_on, intercalate
import qualified data.text.io as T

def main():
    T.putStrLn(intercalate(".", split_on(",", "Hello,How,Are,You,Today")))