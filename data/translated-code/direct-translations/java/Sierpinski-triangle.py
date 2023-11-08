def main():
    print(get_sierpinski_triangle(4))

def get_sierpinski_triangle(n):
    if n == 0:
        return "*"
    
    s = get_sierpinski_triangle(n-1)
    split = s.split("\n")
    length = len(split)

    # Top triangle
    sb = ""
    top = build_space(2 ** (n-1))
    for i in range(length):
        sb += top + split[i] + "\n"
    
    # Two triangles side by side
    for i in range(length):
        sb += split[i] + build_space(length-i) + split[i] + "\n"
    
    return sb

def build_space(n):
    return " " * n

if __name__ == "__main__":
    main()