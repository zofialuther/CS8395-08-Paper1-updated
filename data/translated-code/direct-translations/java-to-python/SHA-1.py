```python
import hashlib

def messageDigest(message):
    state = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]

    def addPadding(message):
        bytes_message = message.encode('utf-8')
        bytes_message += b'\x80'
        padding = (56 - len(bytes_message) % 64) % 64
        bytes_message += b'\x00' * padding
        bit_length = len(message) * 8
        bytes_message += bit_length.to_bytes(8, byteorder='big')
        return bytes_message

    def process_chunk(chunk, state):
        w = [0] * 80
        for i in range(0, len(chunk), 4):
            w[i // 4] = int.from_bytes(chunk[i:i+4], byteorder='big')

        for i in range(16, 80):
            w[i] = (w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]) << 1
            w[i] &= 0xffffffff

        a, b, c, d, e = state
        for i in range(80):
            if i // 20 == 0:
                f = (b & c) | ((~b) & d)
                k = 0x5a827999
            elif i // 20 == 1:
                f = b ^ c ^ d
                k = 0x6ed9eba1
            elif i // 20 == 2:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8f1bbcdc
            else:
                f = b ^ c ^ d
                k = 0xca62c1d6

            temp = ((a << 5) | (a >> 27)) + f + e + k + w[i]
            temp &= 0xffffffff
            e, d, c, b, a = d, c, ((b << 30) | (b >> 2)), a, temp

        state[0] = (state[0] + a) & 0xffffffff
        state[1] = (state[1] + b) & 0xffffffff
        state[2] = (state[2] + c) & 0xffffffff
        state[3] = (state[3] + d) & 0xffffffff
        state[4] = (state[4] + e) & 0xffffffff

    padded_message = addPadding(message)
    for i in range(0, len(padded_message), 64):
        chunk = padded_message[i:i+64]
        process_chunk(chunk, state)

    result = ''.join(format(x, '02x') for x in state)
    return result

print(messageDigest("Rosetta Code"))
```
This Python code uses the hashlib library to implement the SHA1 algorithm and print the message digest of "Rosetta Code".