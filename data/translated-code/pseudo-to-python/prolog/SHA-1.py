import hashlib

def sha_hex(Str, Hex):
    Hash = hashlib.sha256(Str.encode()).hexdigest()
    Hex = Hash