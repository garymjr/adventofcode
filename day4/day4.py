import hashlib

secret_key = 'yzbqklnj'

def find_hash(data, match):
    md5 = hashlib.md5()
    md5.update(bytes(data, 'utf8'))
    return md5.hexdigest().startswith(match)

# part 1
i = 0
while find_hash(secret_key + str(i), '00000') == False:
    i += 1

# part 2
j = 0
while find_hash(secret_key + str(j), '000000') == False:
    j += 1

print(i, j)