def lookandsay(num):
    result = ""
    i = 0
    while i < len(num):
        count = 1
        while i + 1 < len(num) and num[i] == num[i + 1]:
            count += 1
            i += 1
        result += str(count) + num[i]
        i += 1
    return result

def main():
    num = "1"
    for i in range(10):
        print(num)
        num = lookandsay(num)