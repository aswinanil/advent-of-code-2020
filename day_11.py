file_handle = open('input/input_day_11.txt')
seats = [list(line) for line in file_handle.read().splitlines()]

outside = ['o' for i in range(len(seats[0]))]
seats.append(outside)
seats.insert(0, outside.copy())

for seat in seats:
    seat.append('o')
    seat.insert(0, 'o')

def get_num_adjacent_occupied(seats, i, j):
    perimeter_coordinates = [(i-1, j-1), (i, j-1), (i+1, j-1)]
    perimeter_coordinates.extend([(i-1, j), (i+1, j)])
    perimeter_coordinates.extend([(i-1, j+1), (i, j+1), (i+1, j+1)])

    count_adjacent_occupied = 0
    for (x, y) in perimeter_coordinates:
        if seats[x][y] == "#":
            count_adjacent_occupied += 1

    return count_adjacent_occupied

def has_visible_occupied_in_direction(seats, i, j, i_increment, j_increment):
    i += i_increment
    j += j_increment
    seat = seats[i][j]

    while seat != 'o':
        if seat == '#':
            return True
        elif seat == 'L':
            return False

        i += i_increment
        j += j_increment
        seat = seats[i][j]

    return False

directions = {
    'top_left': (-1, 1),
    'top': (0, 1),
    'top_right': (1, 1),
    'right': (1, 0),
    'btm_right': (1, -1),
    'btm': (0, -1),
    'btm_left': (-1, -1),
    'left': (-1, 0)
}
def get_num_visible_occupied(seats, i, j):
    count_adjacent_occupied = 0

    for direction in directions:
        (i_increment, j_increment) = directions[direction]
        count_adjacent_occupied += 1 if has_visible_occupied_in_direction(seats, i, j, i_increment, j_increment) else 0

    return count_adjacent_occupied

def get_new_seat(seats, i, j):
    seat = seats[i][j]

    if seat == 'L' and get_num_adjacent_occupied(seats, i, j) == 0:
        return '#'
    elif seat == '#' and get_num_adjacent_occupied(seats, i, j) > 3:
        return 'L'
    else:
        return seat

def get_new_seat_part_2(seats, i, j):
    seat = seats[i][j]

    if seat == 'L' and get_num_visible_occupied(seats, i, j) == 0:
        return '#'
    elif seat == '#' and get_num_visible_occupied(seats, i, j) > 4:
        return 'L'
    else:
        return seat

def get_new_seats(seats, is_part_2):
    new_seats = [row[:] for row in seats]
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            new_seats[i][j] = get_new_seat(seats, i, j) if not is_part_2 else get_new_seat_part_2(seats, i, j)

    return new_seats

def get_final_occupied_count(is_part_2):
    before = []
    current = seats
    while before != current:
        before = current
        current = get_new_seats(before, is_part_2)

    count_occupied_final = 0
    for row in before:
        for seat in row:
            if seat == '#':
                count_occupied_final += 1

    return count_occupied_final

print(get_final_occupied_count(False))  # Part 1
print(get_final_occupied_count(True))  # Part 2
