class BalancedTernary:
    def __init__(self, s):
        i = 0
        while s[i] == '0':
            i += 1
        self.value = s[i:]

    def convertToBT(self, v):
        if v < 0:
            return self.flip(self.convertToBT(-v))
        if v == 0:
            return ""
        rem = self.mod3(v)
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
            sum += dig * (3 ** i)
        return sum

    def add(self, that):
        a = self.value
        b = that.value
        longer = a if len(a) > len(b) else b
        shorter = a if len(a) > len(b) else b
        while len(shorter) < len(longer):
            shorter = '0' + shorter
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
        return BalancedTernary(sum)

    def addDigits(self, a, b, carry='0'):
        sum1 = self.addDigits(a, b)
        sum2 = self.addDigits(sum1[-1], carry)
        if len(sum1) == 1:
            return sum2
        if len(sum2) == 1:
            return sum1[0] + sum2
        return sum1[0]

    def addDigits(self, a, b):
        if a == '0':
            return b
        elif b == '0':
            return a
        elif a == '+':
            if b == '+':
                return "+-"
            else:
                return "0"
        else:
            if b == '+':
                return "0"
            else:
                return "-+"

    def neg(self):
        return BalancedTernary(self.flip(self.value))

    def sub(self, that):
        return self.add(that.neg())

    def mul(self, that):
        one = BalancedTernary(1)
        zero = BalancedTernary(0)
        mul = BalancedTernary(0)
        flipflag = 0
        if that.compareTo(zero) == -1:
            that = that.neg()
            flipflag = 1
        for i in range(1, that.intValue() + 1):
            mul = mul.add(self)
        if flipflag == 1:
            mul = mul.neg()
        return mul

    def equals(self, that):
        return self.value == that.value

    def compareTo(self, that):
        if self.intValue() > that.intValue():
            return 1
        elif self.equals(that):
            return 0
        return -1

    def __str__(self):
        return self.value


a = BalancedTernary("+-0++0+")
b = BalancedTernary(-436)
c = BalancedTernary("+-++-")

print("a=", a.intValue())
print("b=", b.intValue())
print("c=", c.intValue())
print()

result = a.mul(b.sub(c))

print("result=", result, result.intValue())