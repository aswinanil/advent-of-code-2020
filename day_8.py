import pdb

# file_handle = open('input_day_8_example.txt')
file_handle = open('input_day_8.txt')
lines = file_handle.read().splitlines()
instructions = [line.split(' ') for line in lines]

def have_duplicate():
    return len(i_sequence) != len(set(i_sequence))

acc = 0
i = 0
i_sequence = []

def execute(cmd, arg):
    global acc, i

    if cmd == 'acc':
        acc += arg
    elif cmd == 'jmp':
        i += arg

while i < len(instructions):
    i_sequence.append(i)
    if have_duplicate():
        break

    [cmd, arg] = instructions[i]
    execute(cmd, int(arg))

    if (cmd != 'jmp'):
        i += 1

print(acc)
