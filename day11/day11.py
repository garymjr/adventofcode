import re

def test_password(password):
    test1 = False
    test2 = False
    test3 = False
    # test 1 - must include increasing straight of at least 3 letters
    password = list(map(ord, list(password)))
    for i in range(len(password) - 2):
        if (password[i] + 1) == password[i+1] and (password[i] + 2) == password[i+2]:
            test1 = True

    # test 2 - must not contain i, o or l
    password = "".join(list(map(chr, password)))
    if re.search(r'(i|o|l)', password) == None:
        test2 = True

    # test 3 - must have two non-overlapping pairs
    if re.search(r'([a-z])\1[a-z]*([a-z])\2', password) != None:
        test3 = True

    return test1 and test2 and test3

def create_password(base):
    offset = 1
    wrapped = True
    password = list(base)

    while wrapped == True and offset <= len(password):
        i = -offset
        if ord(password[i]) == 122:
            password[i] = "a"
        else:
            password[i] = chr(ord(password[i]) + 1)
            wrapped = False
        offset += 1

    return "".join(password)


password = create_password("vzbxkghb")
while test_password(password) == False:
    password = create_password(password)
print(password)

password = create_password(password)
while test_password(password) == False:
    password = create_password(password)
print(password)
