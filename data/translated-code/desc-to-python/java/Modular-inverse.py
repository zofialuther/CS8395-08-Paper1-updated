from Crypto.Util.number import BigInteger

num = BigInteger(42)
mod = BigInteger(2017)

result = num.inverse(mod)
print(result)