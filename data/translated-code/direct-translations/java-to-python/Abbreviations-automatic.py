```python
import os

def main():
    path = "days_of_week.txt"
    with open(path, 'r') as file:
        read_all_lines = file.readlines()
        for i, line in enumerate(read_all_lines):
            line = line.strip()
            if len(line) == 0:
                continue

            days = line.split(" ")
            if len(days) != 7:
                raise RuntimeError("There aren't 7 days on line " + str(i + 1))

            temp = {}
            for day in days:
                if day in temp:
                    temp[day] += 1
                else:
                    temp[day] = 1
            if len(temp) < 7:
                print(" ∞  " + line)
                continue

            len_ = 1
            while True:
                temp.clear()
                for day in days:
                    sd = day if len_ >= len(day) else day[:len_]
                    if sd in temp:
                        temp[sd] += 1
                    else:
                        temp[sd] = 1
                if len(temp) == 7:
                    print(f"{len_:2d}  {line}")
                    break
                len_ += 1

if __name__ == "__main__":
    main()
```