```python
import hashlib

def messageDigest(message):
    state = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]

    bytes = addPadding(message)
    for i in range(len(bytes) // 64):
        values = [0] * 80
        for j in range(64):
            values[j // 4] |= (bytes[i * 64 + j] & 0xff) << ((3 - j % 4) * 8)
        for j in range(16, 80):
            values[j] = (values[j - 3] ^ values[j - 8] ^ values[j - 14] ^ values[j - 16]) << 1

        a, b, c, d, e = state[0], state[1], state[2], state[3], state[4]
        f, k = 0, 0
        for j in range(80):
            if j // 20 == 0:
                f = (b & c) | (~b & d)
                k = 0x5a827999
            elif j // 20 == 1:
                f = b ^ c ^ d
                k = 0x6ed9eba1
            elif j // 20 == 2:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8f1bbcdc
            elif j // 20 == 3:
                f = b ^ c ^ d
                k = 0xca62c1d6

            temp = (a << 5 & 0xffffffff) + f + e + k + values[j] & 0xffffffff
            e, d, c, b, a = d & 0xffffffff, c & 0xffffffff, (b << 30 | b >> 2) & 0xffffffff, a & 0xffffffff, temp & 0xffffffff

        state[0] = (state[0] + a) & 0xffffffff
        state[1] = (state[1] + b) & 0xffffffff
        state[2] = (state[2] + c) & 0xffffffff
        state[3] = (state[3] + d) & 0xffffffff
        state[4] = (state[4] + e) & 0xffffffff

    result = ""
    for i in range(20):
        result += format((state[i // 4] >> 24 - (i % 4) * 8) & 0xFF, '02x')

    return result

def addPadding(message):
    bytes = message.encode('utf-8')
    bytes += b'\x80'
    padding = 64 - (len(bytes) % 64)
    if padding < 8:
        padding += 64
    bytes += b'\x00' * padding
    bit_length = len(message) * 8
    bytes += bit_length.to_bytes(8, 'big')
    return bytes

print(messageDigest("Rosetta Code"))
```