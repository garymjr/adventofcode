def look_and_say(val):
    res = []
    count = 0
    previous_char = None

    for v in val:
        if previous_char is not None and v != previous_char:
            res.extend([str(count), previous_char])
            count = 0
        previous_char = v
        count += 1
    res.extend([str(count), previous_char])
    return "".join(res)

sequence = "1321131112"
for _ in range(40):
    sequence = look_and_say(sequence)
print(len(sequence))

for _ in range(10):
    sequence = look_and_say(sequence)
print(len(sequence))
