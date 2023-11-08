from Crypto.PublicKey import RSA

# Create a BigInteger object and assign the value 42 to it
num1 = RSA.importKey(42)

# Create another BigInteger object and assign the value 2017 to it
num2 = RSA.importKey(2017)

# Call the modInverse method on the first BigInteger object, passing the second BigInteger object as an argument
result = num1.modInverse(num2)

# Print the result of the modInverse method to the console
print(result)