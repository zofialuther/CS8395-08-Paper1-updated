import Data.ByteString.Lazy.Char8 as C

def main():
    with open("data.txt", "r") as file:
        cs = C.readFile(file.read())
        lines = cs.splitlines()
        for x in lines:
            if 6 < float(x.split()[-1]):
                print(x)