```python
class Hailstone:

    @staticmethod
    def get_hailstone_sequence(n):
        if n <= 0:
            raise ValueError("Invalid starting sequence number")
        list = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            list.append(n)
        return list

    @staticmethod
    def main():
        sequence27 = Hailstone.get_hailstone_sequence(27)
        print(f"Sequence for 27 has {len(sequence27)} elements: {sequence27}")

        MAX = 100000
        # Simple way
        highest_number = 1
        highest_count = 1
        for i in range(2, MAX):
            count = len(Hailstone.get_hailstone_sequence(i))
            if count > highest_count:
                highest_count = count
                highest_number = i
        print(f"Method 1, number {highest_number} has the longest sequence, with a length of {highest_count}")

        # More memory efficient way
        highest_number = 1
        highest_count = 1
        for i in range(2, MAX):
            count = 1
            n = i
            while n != 1:
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = 3 * n + 1
                count += 1
            if count > highest_count:
                highest_count = count
                highest_number = i
        print(f"Method 2, number {highest_number} has the longest sequence, with a length of {highest_count}")

        # Efficient for analyzing all sequences
        highest_number = 1
        highest_count = 1
        sequence_map = {1: 1}
        for i in range(2, MAX):
            current_list = []
            n = i
            while n not in sequence_map:
                current_list.append(n)
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = 3 * n + 1
            cur_count = sequence_map[n]
            for j in reversed(current_list):
                cur_count += 1
                sequence_map[j] = cur_count
            if cur_count > highest_count:
                highest_count = cur_count
                highest_number = i
        print(f"Method 3, number {highest_number} has the longest sequence, with a length of {highest_count}")


Hailstone.main()
```