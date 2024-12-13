import hashlib

data = 'ckczppom'
index = 1
while True:
    salted = data + str(index)
    digest = hashlib.md5(salted.encode('ascii')).hexdigest()
    if digest[0:5] == '00000':
        break
    index += 1
print(index)
