import re

f = open("./input.txt")
lines = f.readlines()
wires = {}

def get_val(wire):
    if wire.isdigit():
        val = int(wire)
    elif wire in wires.keys():
        val = wires[wire]
    else:
        val = find_wire_val(wire)
    return val


def find_wire_val(wire):
    if wire in wires.keys():
        return wires[wire]

    for line in lines:
        line = line.split()
        output_wire = line[-1]

        if wire == output_wire:
            if len(line) == 3:
                wires[output_wire] = get_val(line[0])
            elif line[0] == "NOT":
                wires[output_wire] = 65535 - get_val(line[1])
            elif line[1] == "AND":
                wires[output_wire] = get_val(line[0]) & get_val(line[2])
            elif line[1] == "OR":
                wires[output_wire] = get_val(line[0]) | get_val(line[2])
            elif line[1] == "LSHIFT":
                shift = int(line[2])
                wires[output_wire] = get_val(line[0]) << shift
            elif line[1] == "RSHIFT":
                shift = int(line[2])
                wires[output_wire] = get_val(line[0]) >> shift
    return wires[wire]

# part 1
print(find_wire_val("a"))

# part 2
b = wires['a']
wires.clear()
wires['b'] = b
print(find_wire_val("a"))
