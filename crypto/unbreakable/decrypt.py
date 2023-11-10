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

