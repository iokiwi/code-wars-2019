from base64 import b64encode


def encrypt(key, secret):
    out = ""
    for i in range(len(secret)):
        out += chr(ord(key[i % len(key)]) ^ ord(secret[i]))
    return out


def encode(s):
    return b64encode(str.encode(s))


a = encrypt("abc", "Hello, World!")
print(encode(a))
print(encrypt("Hello, World!", a))
