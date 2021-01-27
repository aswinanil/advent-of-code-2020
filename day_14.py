file_handle = open('input_day_14.txt')
instructions = [line.split(' = ') for line in file_handle.read().splitlines()]

memory = {}

def get_binary_list(value):
    return list(f'{value:036b}')

def get_decimal_value(binary_list):
    return int(''.join(binary_list), 2)

def get_masked_value(value, mask):
    value = get_binary_list(value)

    for i in range(len(mask)):
        if mask[i] != 'X':
            value[i] = mask[i]

    return int(''.join(value), 2)

def get_masked_address(address, mask):
    address_binary = get_binary_list(int(address))

    for i in range(len(mask)):
        if mask[i] == 'X':
            address_binary[i] = 'X'
        elif mask[i] == '1':
            address_binary[i] = '1'

    return address_binary

def get_permutations(masked_address):
    i = masked_address.index('X')
    [first, second] = [masked_address.copy(), masked_address.copy()]
    first[i] = '1'
    second[i] = '0'
    return [first, second]

def get_all_addresses(masked_address):
    addresses = []
    masked_addresses = [masked_address]

    while masked_addresses:
        permutations = get_permutations(masked_addresses.pop())
        if 'X' in permutations[0]:
            masked_addresses.extend(permutations)
        else:
            addresses.extend(permutations)

    return addresses

def execute(instruction, mask):
    [address, value] = instruction
    address = int(address[4:][:-1])
    memory[address] = get_masked_value(int(value), list(mask))

def execute_v2(instruction, mask):
    [address, value] = instruction
    masked_address = get_masked_address(address[4:][:-1], mask)
    all_addresses = get_all_addresses(masked_address)

    for address in all_addresses:
        address = get_decimal_value(address)
        memory[address] = int(value)

def get_sum(is_v2):
    global instructions, memory

    for instruction in instructions:
        if 'mask' in instruction:
            mask = instruction[1]
        else:
            execute(instruction, mask) if not is_v2 else execute_v2(instruction, mask)

    sum = 0
    for address in memory:
        sum += memory[address]
    return sum


# Part 1
print(get_sum(False))

# Part 2
memory = {}
print(get_sum(True))
