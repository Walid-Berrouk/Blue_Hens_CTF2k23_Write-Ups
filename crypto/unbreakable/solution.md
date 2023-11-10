# unbreakable 

## Description

> https://github.com/Lukerd-29-00/unbreakable

## Write-Up

As we are given two files : `flag.enc` where the encrypted flag is stored, and a cryptogramm based on **AES Symmetric encryption**:

```py
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
key = os.urandom(16)

with open("flag.txt","r") as f:
    flag = f.read().strip().encode()

iv = os.urandom(AES.block_size)

ct = AES.new(key,AES.MODE_CBC,iv).encrypt(pad(flag,AES.block_size))

with open("flag.enc","wb") as f:
    f.write(iv + ct)
```

As we can see, the key here is randomly set. But when we dive deeper in the given repository, we can see that the password was set in previous version:

```py
...
key = hashlib.sha256(b"tasciewapeoiu").digest()
...
```

From there, we can use it to decrypt the flag. To do that, we just need to create a code to decrypt an AES encrypted data:

```py
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# Key (should be the same as the one used for encryption)
key = hashlib.sha256(b"tasciewapeoiu").digest()

# Read the encrypted file
with open("flag.enc", "rb") as f:
    encrypted_data = f.read()

# Extract IV and ciphertext
iv = encrypted_data[:AES.block_size]
ct = encrypted_data[AES.block_size:]

# Initialize AES decryption cipher
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the ciphertext
pt = cipher.decrypt(ct)

# Remove PKCS7 padding
padding_length = pt[-1]
pt = pt[:-padding_length]

# Convert the plaintext to a string and print it
plaintext = pt.decode()
print(plaintext)
```


## Flag

UDCTF{N0th1ng_pr0t3cts_4gainst_5l0ppiness}