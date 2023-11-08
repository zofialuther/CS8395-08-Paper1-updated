```python
# Python program to generate and print the first 72 upper case and lower case letters in the Unicode character set

# using range() to generate a range of Unicode code points
# filtering the code points based on whether they are upper case or lower case letters
upper_case_letters = [chr(i) for i in range(65, 65+26)]
lower_case_letters = [chr(i) for i in range(97, 97+26)]

# printing the filtered code points as characters
print("Upper case letters:", upper_case_letters)
print("Lower case letters:", lower_case_letters)
```