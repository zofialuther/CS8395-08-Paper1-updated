```python
class AliquotSequenceClassifications:
    def properDivsSum(self, num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum
    
    def aliquot(self, num, max_length, max_term):
        sequence = [num]
        current_term = num
        for _ in range(max_length):
            if current_term == 0 or current_term == 1:
                break
            elif current_term > max_term:
                break
            elif current_term in sequence[:-1]:
                sequence.append(current_term)
                break
            else:
                current_term = self.properDivsSum(current_term)
                sequence.append(current_term)
        # Classification logic here
        return sequence
    
    def report(self, sequence):
        print(sequence)
        # Print classification results
    
    def main(self):
        numbers = [28, 220, 284, 1184, 1210, 2924, 5020]
        for num in numbers:
            sequence = self.aliquot(num, 100, 10**6)
            self.report(sequence)

# Instantiate the class and run the main method
obj = AliquotSequenceClassifications()
obj.main()
```