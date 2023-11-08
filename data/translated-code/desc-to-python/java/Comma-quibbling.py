```python
class Quibbler:
    def quibble(self, arr):
        formatted_string = ''
        for i in range(len(arr)):
            if i != len(arr) - 1:
                formatted_string += arr[i] + ', '
            else:
                formatted_string += 'and ' + arr[i]
        return formatted_string

    def main(self):
        arr1 = ['apple', 'banana', 'orange']
        arr2 = ['dog', 'cat', 'bird', 'fish']
        print(self.quibble(arr1))
        print(self.quibble(arr2))

quibbler = Quibbler()
quibbler.main()
```