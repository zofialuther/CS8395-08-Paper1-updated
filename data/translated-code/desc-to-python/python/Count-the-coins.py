import importlib

try:
    importlib.import_module('psyco')
    import psyco
    psyco.full()
except ImportError:
    pass

def count_changes(amount, coins):
    # function implementation

def main():
    # test count_changes function with different amounts and sets of coins
    # print the results

if __name__ == "__main__":
    main()