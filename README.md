# PythonFileEncryption
This is a simple Python script with basic file encryption and decryption functionality using XOR

# How It Works
- Each byte is XORed with a user-provided key
- The same key can encrypt and decrypt the file
-

# What is XOR
- bitwise encryption method
  - compares two bits
  - returns 1 if the bits are different
  - returns 0 if the bits are the same
- useful for basic data transformation
- each byte of data is combined with an encryption key using XOR
- Pros:
  - fast and easy to implement
- Cons:
  - not secure, do not use for protecting sensitive data