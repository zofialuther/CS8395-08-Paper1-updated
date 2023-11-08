def repeat(str, times):
    sb = ""
    for i in range(times):
        sb += str
    return sb

def main():
    print(repeat("ha", 5))

main()