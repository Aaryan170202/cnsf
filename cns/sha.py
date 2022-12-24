import hashlib

#encode
text = hashlib.sha1(b'helllllo')

#convert
encrypt = text.hexdigest()

print(encrypt)