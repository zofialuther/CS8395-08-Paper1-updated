import hashlib

def sha_hex(Str):
    hash_object = hashlib.sha1(Str.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig