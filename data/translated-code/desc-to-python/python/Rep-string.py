def is_repeated(s):
    for i in range(1, len(s)):
        if s[:i] * (len(s)//i) + s[:len(s)%i] == s:
            print(f"{s} has a repetition of length {i} with the substring {s[:i]}")
            return
    print(f"{s} does not have a repetition")
    
strings = ["hellohello", "goodbye", "yesyesyes", "abcabcabc"]
for string in strings:
    is_repeated(string)