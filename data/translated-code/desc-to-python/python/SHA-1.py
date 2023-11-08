import hashlib

string = "Ars longa, vita brevis"
encoded_string = string.encode('ascii')

hash_object = hashlib.sha1(encoded_string)
hash_value = hash_object.hexdigest()

print(hash_value)