```python
class Hailstone:
    
    def generate_hailstone_sequence(self, num):
        sequence = [num]
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            sequence.append(num)
        return sequence

    def simple_method(self):
        longest_sequence = []
        max_length = 0
        for i in range(1, 100001):
            sequence = self.generate_hailstone_sequence(i)
            if len(sequence) > max_length:
                max_length = len(sequence)
                longest_sequence = sequence
        print("Simple Method: Number with longest sequence -", longest_sequence[0], "Length -", max_length)

    def memory_efficient_method(self):
        sequence_lengths = {}
        max_length = 0
        for i in range(1, 100001):
            num = i
            length = 0
            while num != 1:
                if num in sequence_lengths:
                    length += sequence_lengths[num]
                    break
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
                length += 1
            sequence_lengths[i] = length
            if length > max_length:
                max_length = length
                longest_sequence = i
        print("Memory Efficient Method: Number with longest sequence -", longest_sequence, "Length -", max_length)

    def efficient_method(self):
        max_length = 0
        for i in range(1, 100001):
            num = i
            length = 0
            while num != 1:
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
                length += 1
            if length > max_length:
                max_length = length
                longest_sequence = i
        print("Efficient Method: Number with longest sequence -", longest_sequence, "Length -", max_length)


h = Hailstone()
h.simple_method()
h.memory_efficient_method()
h.efficient_method()
```