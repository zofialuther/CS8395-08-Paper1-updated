```python
# Simulation of 100 doors and their states
for i in range(1, 101):
    if i**0.5 == int(i**0.5):
        print(f"Door {i} is open")
    else:
        print(f"Door {i} is closed")
```