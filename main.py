import hashlib


text=input("enter the text or string: ")

hash_obj = hashlib.md5(text.encode())
md5_hash = hash_obj.hexdigest()

print(md5_hash)