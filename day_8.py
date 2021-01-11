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

def run_instructions(instructions):
    global i, i_sequence

    has_duplicate = False
    while i < len(instructions):
        i_sequence.append(i)
        if have_duplicate():
            has_duplicate = True
            break

        [cmd, arg] = instructions[i]
        execute(cmd, int(arg))

        if (cmd != 'jmp'):
            i += 1

    # Part 2
    if not has_duplicate:
        print(acc)

# Part 1
run_instructions(instructions)
print(acc)


# Part 2
for i in range(len(instructions)):
    [cmd, arg] = instructions[i]

    if cmd == 'acc':
        continue
    elif cmd == 'jmp':
        cmd = 'nop'
    else:
        cmd = 'jmp'

    instructions_copy = instructions.copy()
    instruction_copy = instructions[i].copy()
    instruction_copy[0] = cmd
    instructions_copy[i] = instruction_copy

    acc = 0
    i = 0
    i_sequence = []
    run_instructions(instructions_copy)
