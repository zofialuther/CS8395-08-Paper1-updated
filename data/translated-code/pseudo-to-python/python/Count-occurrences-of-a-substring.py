def countSubstring(s, sub):
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            count = count + 1
    return count

print(countSubstring("the three truths", "th"))
print(countSubstring("ababababab", "abab"))