def main():
    Printer = open("/dev/lp0", "w")
    Printer.write("Hello, world!")
    Printer.flush()
    Printer.close()

main()