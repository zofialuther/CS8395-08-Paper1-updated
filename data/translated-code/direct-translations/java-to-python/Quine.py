class S:
    def main(a):
        s = "class S{public static void main(String[]a){String s=;char c=34;System.out.println(s.substring(0,52)+c+s+c+s.substring(52));}}"
        c = 34
        print(s[0:52] + chr(c) + s + chr(c) + s[52:])