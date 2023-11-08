```python
values = ['1.2.3', '5.4.3', '2.3.1', '3.2.5']
sorted_values = sorted(values, key=lambda x: [int(i) for i in x.split('.')])
print(sorted_values)
```