```python
with open('/dev/lp0', 'w') as printer:
    printer.write('Hello, world!')
    printer.flush()
```