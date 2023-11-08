from itertools import groupby

def collapser(txt):
    return ''.join(item for item, grp in groupby(txt))

if __name__ == '__main__':
    strings = [
            "",
            '"If I were two-faced, would I be wearing this one?" --- Abraham Lincoln ',
            "..1111111111111111111111111111111111111111111111111111111111111117777888",
            "I never give 'em hell, I just tell the truth, and they think it's hell. ",
            "                                                   ---  Harry S Truman  ",
            "The better the 4-wheel drive, the further you'll be from help when ya get stuck!",
            "headmistressship",
            "aardvark",
            "😍😀🙌💃😍😍😍🙌",
            ]
    for txt in strings:
        this = "Original"
        print("\n{:14} Size: {} «««{}»»»".format(this, len(txt), txt))
        this = "Collapsed"
        sqz = collapser(txt)
        print("{:>14} Size: {} «««{}»»»".format(this, len(sqz), sqz))