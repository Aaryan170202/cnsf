import hashlib
import base32hex
txt=hashlib.sha1(b"Hello World")
encrypt=txt.hexdigest()
print(encrypt)