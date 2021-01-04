import pdb

# file_handle = open('input_day_14_example.txt')
file_handle = open('input_day_14.txt')
instructions = [line.split(' = ') for line in file_handle.read().splitlines()]

memory = {}

def get_masked_value(value, mask):
    value = list(f'{value:036b}')

    for i in range(len(mask)):
        if mask[i] != 'X':
            value[i] = mask[i]

    return int(''.join(value), 2)

def execute(instruction, mask):
    [address, value] = instruction
    address = address[4:][:-1]
    memory[address] = get_masked_value(int(value), list(mask))

for instruction in instructions:
    if 'mask' in instruction:
        mask = instruction[1]
    else:
        execute(instruction, mask)

sum = 0
for address in memory:
    sum += memory[address]

print(sum)
