from pathlib import Path

class Abbreviations:
    def main(args):
        try:
            file_path = Path("days_of_week.txt")
            readAllLines = file_path.read_text().splitlines()

            for i in range(len(readAllLines)):
                line = readAllLines[i]
                if len(line) == 0:
                    continue
                days = line.split(" ")
                if len(days) != 7:
                    raise RuntimeError(f"There aren't 7 days on line {i + 1}")

                temp = {}
                for day in days:
                    count = temp.get(day, 0)
                    temp[day] = count + 1

                if len(temp) < 7:
                    print(" ∞  ", line)
                    continue

                len = 1
                while True:
                    temp.clear()
                    for day in days:
                        if len >= len(day):
                            sd = day
                        else:
                            sd = day[:len]
                        count = temp.get(sd, 0)
                        temp[sd] = count + 1

                    if len(temp) == 7:
                        print(f"{len}  {line}")
                        break

                    len += 1
        except Exception as e:
            print(e)