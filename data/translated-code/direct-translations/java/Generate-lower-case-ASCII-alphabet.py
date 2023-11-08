class LowerAscii:
    def main(self):
        sb = ""
        for ch in range(ord('a'), ord('z')+1):
            sb += chr(ch)
        print("lower ascii: " + sb + ", length: " + str(len(sb)))

lower_ascii = LowerAscii()
lower_ascii.main()