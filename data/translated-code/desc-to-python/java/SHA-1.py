```python
import hashlib

class SHA1:
    def __init__(self, message):
        self.message = message

    def generate_hash(self):
        sha1 = hashlib.sha1()
        sha1.update(self.message.encode('utf-8'))
        return sha1.hexdigest()

class SHA1Task:
    @staticmethod
    def main():
        message = "Rosetta Code"
        sha1 = SHA1(message)
        hash_value = sha1.generate_hash()
        print(hash_value)

SHA1Task.main()
```