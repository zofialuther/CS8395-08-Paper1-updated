```python
count = 0
for police in range(13):
    for sanitation in range(13):
        for fire in range(13):
            if (police + sanitation + fire) == 12:
                print(f"Police: {police}, Sanitation: {sanitation}, Fire: {fire}")
                count += 1
print(f"Total number of valid combinations: {count}")
```