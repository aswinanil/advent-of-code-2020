file_handle = open('input/input_day_12.txt')
instructions = [(line[0], int(line[1:])) for line in file_handle.read().splitlines()]

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

def set_new_direction_waypoint(action, value):
    global waypoint_east, waypoint_north

    value %= 360
    direction_multiplier = 1 if action == 'R' else -1

    for i in range(0, value, 90):
        temp = waypoint_north
        waypoint_north = direction_multiplier * -waypoint_east
        waypoint_east = direction_multiplier * temp

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

def perform_action_waypoint(action, value):
    global east, north, waypoint_east, waypoint_north

    if action == 'N':
        waypoint_north += value
    elif action == 'S':
        waypoint_north -= value
    elif action == 'E':
        waypoint_east += value
    elif action == 'W':
        waypoint_east -= value
    elif action == 'L' or action == 'R':
        set_new_direction_waypoint(action, value)
    elif action == 'F':
        north += waypoint_north * value
        east += waypoint_east * value
    else:
        print('unexpected input')

# Part 1
east = 0
north = 0
current_direction = 'E'

for (action, value) in instructions:
    perform_action(action, value)

print(abs(east) + abs(north))


# Part 2
east = 0
north = 0
waypoint_east = 10  # relative to ship
waypoint_north = 1  # relative to ship

for (action, value) in instructions:
    perform_action_waypoint(action, value)

print(abs(east) + abs(north))
