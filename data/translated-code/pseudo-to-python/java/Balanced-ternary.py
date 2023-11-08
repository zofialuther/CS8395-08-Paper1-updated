class BTernary:
    def __init__(self, s):
        i = 0
        while s[i] == '0':
            i += 1
        self.value = s[i:]

    def __init__(self, v):
        self.value = ""
        self.value = self.convertToBT(v)

    def convertToBT(self, v):
        if v < 0:
            return self.flip(self.convertToBT(-v))
        if v == 0:
            return ""
        rem = v % 3
        if rem == 0:
            return self.convertToBT(v // 3) + "0"
        if rem == 1:
            return self.convertToBT(v // 3) + "+"
        if rem == 2:
            return self.convertToBT((v + 1) // 3) + "-"
        return "You can't see me"

    def flip(self, s):
        flip = ""
        for i in range(len(s)):
            if s[i] == '+':
                flip += '-'
            elif s[i] == '-':
                flip += '+'
            else:
                flip += '0'
        return flip

    def mod3(self, v):
        if v > 0:
            return v % 3
        v = v % 3
        return (v + 3) % 3

    def intValue(self):
        sum = 0
        s = self.value
        for i in range(len(s)):
            c = s[len(s) - i - 1]
            dig = 0
            if c == '+':
                dig = 1
            elif c == '-':
                dig = -1
            sum += dig * (3**i)
        return sum

    def add(self, that):
        a = self.value
        b = that.value

        longer = a if len(a) > len(b) else b
        shorter = b if len(a) > len(b) else a

        while len(shorter) < len(longer):
            shorter = "0" + shorter

        a = longer
        b = shorter

        carry = '0'
        sum = ""
        for i in range(len(a)):
            place = len(a) - i - 1
            digisum = self.addDigits(a[place], b[place], carry)
            if len(digisum) != 1:
                carry = digisum[0]
            else:
                carry = '0'
            sum = digisum[-1] + sum
        sum = carry + sum

        return BTernary(sum)