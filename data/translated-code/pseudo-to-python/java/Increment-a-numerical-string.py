from decimal import Decimal

s = "123456789012345678901234567890.12345"
s = Decimal(s) + 1
s = str(s)