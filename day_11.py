import pdb

# file_handle = open('input_day_11_example.txt')
file_handle = open('input_day_11.txt')
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

def get_new_seat(seats, i, j):
    seat = seats[i][j]

    if seat == 'L' and get_num_adjacent_occupied(seats, i, j) == 0:
        return '#'
    elif seat == '#' and get_num_adjacent_occupied(seats, i, j) > 3:
        return 'L'
    else:
        return seat

def get_new_seats(seats):
    new_seats = [row[:] for row in seats]
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            new_seats[i][j] = get_new_seat(seats, i, j)

    return new_seats

before = []
current = seats
while before != current:
    before = current
    current = get_new_seats(before)

count_occupied_final = 0
for row in before:
    for seat in row:
        if seat == '#':
            count_occupied_final += 1

print(count_occupied_final)
