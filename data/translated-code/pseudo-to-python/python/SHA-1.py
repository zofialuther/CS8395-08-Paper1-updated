import hashlib
h = hashlib.sha1()
h.update(bytes("Ars longa, vita brevis", encoding="ASCII"))
result = h.hexdigest()
print(result)