from dataclasses import dataclass

@dataclass
class Show:
    name: str
    season: int

def main():
    shows = [
        Show("Show A", 5),
        Show("Show B", 2),
        Show("Show C", 10),
        Show("Show D", 8),
        Show("Show E", 13),
        Show("Show F", 1),
        Show("Show G", 7),
        Show("Show H", 4),
        Show("Show I", 11),
        Show("Show J", 9),
        Show("Show K", 6),
        Show("Show L", 3),
        Show("Show M", 12)
    ]

    result = sorted(shows, key=lambda x: x.season)
    print(result)

main()