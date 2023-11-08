print("abcd".startswith("ab"))  #returns True
print("abcd".endswith("zn"))  #returns False
print("bb" in "abab")  #returns False
print("ab" in "abab")  #returns True
loc = "abab".find("bb")  #returns -1
loc = "abab".find("ab")  #returns 0
loc = "abab".find("ab",loc+1)  #returns 2