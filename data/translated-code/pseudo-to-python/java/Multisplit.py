from typing import List

class MultiSplit:
    @staticmethod
    def main():
        print("Regex split:")
        print(str(MultiSplit.multiSplit("a!===b=!=c", ["==", "!=", "="])))

        print("\n")

        for s in MultiSplit.multiSplit("a!===b=!=c", ["==", "!=", "="]):
            print(s)

    @staticmethod
    def multiSplit(txt: str, separators: List[str]) -> List[str]:
        result = []
        txtLen = len(txt)
        from_index = 0

        for i in range(txtLen):
            for sep in separators:
                sepLen = len(sep)
                if txt[i:i+sepLen] == sep:
                    result.append(txt[from_index:i])
                    from_index = i + sepLen
                    i = from_index - 1
                    break

        if from_index < txtLen:
            result.append(txt[from_index:])

        return result

MultiSplit.main()