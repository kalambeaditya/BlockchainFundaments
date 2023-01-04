import hashlib
str = "SIPNA COET"

print("The hexadecimal equivalent of SHA256 is : ")
print(hashlib.sha256(str.encode()).hexdigest())
print("\r")
print("The hexadecimal equivalent of SHA384 is : ")
print(hashlib.sha384(str.encode()).hexdigest())
print("\r")
print("The hexadecimal equivalent of SHA224 is : ")
print(hashlib.sha224(str.encode()).hexdigest())
print("\r")
print("The hexadecimal equivalent of SHA512 is : ")
print(hashlib.sha512(str.encode()).hexdigest())
print("\r")
print("The hexadecimal equivalent of SHA1 is : ")
print(hashlib.sha1(str.encode()).hexdigest())
