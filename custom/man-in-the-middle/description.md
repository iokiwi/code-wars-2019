# Give encryption algoryth
# Give plain text
# Give cypher text
# Have contestants get the key
# Have contestants use the key to generate a new message

```python
def xor_encrypt(key, secret):
    out = ""
    for i in range(len(secret)):
        out += chr(ord(key[i % len(key)]) ^ ord(secret[i]))
    return out

def encode(s):
    return b64encode(str.encode(s))
```

