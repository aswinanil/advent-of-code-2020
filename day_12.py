import pdb

# file_handle = open('input_day_12_example.txt')
file_handle = open('input_day_12.txt')
instructions = [(line[0], int(line[1:])) for line in file_handle.read().splitlines()]

east = 0
north = 0
current_direction = 'E'

angles = {
    'E': 90,
    'S': 180,
    'W': 270,
    'N': 0,
}
directions = {
    90: 'E',
    180: 'S',
    270: 'W',
    0: 'N'
}

def set_new_direction(action, value):
    global current_direction
    current_angle = angles[current_direction]

    if action == 'R':
        current_angle += value
    else:
        current_angle -= value

    current_angle %= 360
    current_direction = directions[current_angle]

# print('\tdir: ' + current_direction, 'east: ' + str(east), 'north: ' + str(north))
def perform_action(action, value):
    global east, north

    if action == 'N':
        north += value
    elif action == 'S':
        north -= value
    elif action == 'E':
        east += value
    elif action == 'W':
        east -= value
    elif action == 'L' or action == 'R':
        set_new_direction(action, value)
    elif action == 'F':
        perform_action(current_direction, value)
    else:
        print('unexpected input')

    # print(action, value, '\tdir: ' + current_direction, 'east: ' + str(east), 'north: ' + str(north))

for (action, value) in instructions:
    perform_action(action, value)

print(abs(east) + abs(north))
