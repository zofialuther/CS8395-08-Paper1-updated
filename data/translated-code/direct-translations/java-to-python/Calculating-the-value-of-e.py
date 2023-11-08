from decimal import Decimal, ROUND_HALF_UP
import math

# No direct equivalent for java.math.BigInteger in Python

# Example of using BigDecimal in Python
value = Decimal('10.555')
rounded_value = value.quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
print(rounded_value)