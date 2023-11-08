```python
import re

def main():
    print("Regex split:")
    print(re.split("==|!=|=", "a!===b=!=c"))

    print("\nManual split:")
    for s in multi_split("a!===b=!=c", ["==", "!=", "="]):
        print(f'"{s}"', end=" ")

def multi_split(txt, separators):
    result = []
    txt_len = len(txt)
    from_ = 0

    for to in range(txt_len):
        for sep in separators:
            sep_len = len(sep)
            if txt[to:to + sep_len] == sep:
                result.append(txt[from_:to])
                from_ = to + sep_len
                to = from_ - 1  # compensate for the increment
                break

    if from_ < txt_len:
        result.append(txt[from_:])
    return result

if __name__ == "__main__":
    main()
```