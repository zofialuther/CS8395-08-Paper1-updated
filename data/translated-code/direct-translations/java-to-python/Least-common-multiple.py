```python
# Python code

#prompts user for values to find the LCM for, then saves them to m and n
m = int(input("Enter the value of m:"))
n = int(input("Enter the value of n:"))
lcm = m if (n == m or n == 1) else (n if m == 1 else 0)
# this section increases the value of m until it is greater
# than or equal to n, then does it again when the lesser
# becomes the greater--if they aren't equal. If either value is 1,
# no need to calculate
if (lcm == 0):
    mm = m
    nn = n
    while (mm != nn):
        while (mm < nn):
            mm += m
        while (nn < mm):
            nn += n
    lcm = mm

print("lcm(" + str(m) + ", " + str(n) + ") = " + str(lcm))
```