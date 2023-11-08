```python
class LinePrinter:
    def main(self):
        try:
            with open('/dev/lp0', 'w') as printer:
                printer.write("Hello World!")
        except IOError as e:
            print("An error occurred:", e)
```