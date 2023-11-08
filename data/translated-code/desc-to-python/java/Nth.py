class Nth:
    def ordinalAbbrev(self, n):
        if 10 <= n % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
        return str(n) + suffix

if __name__ == "__main__":
    n = Nth()
    for i in range(1, 21):
        print(n.ordinalAbbrev(i))