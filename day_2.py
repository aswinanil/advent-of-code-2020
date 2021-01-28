file_handle = open('input/input_day_2.txt')
lines = file_handle.readlines()
lines_split = [line.split(' ') for line in lines]

lines_parsed = []
for line in lines_split:
    [low, high] = line[0].split('-')
    char = line[1][0]
    min_max = [int(low), int(high)]
    line_parsed = [int(low), int(high), char, line[2].rstrip('\n')]
    lines_parsed.append(line_parsed)

valid_count_part_1 = 0
valid_count_part_2 = 0
for line in lines_parsed:
    [low, high, char, password] = line

    # part 1
    occurences = password.count(char)
    if occurences >= low and occurences <= high:
        valid_count_part_1 += 1

    # part 2
    if high > len(password):
        continue
    first_occured = password[low-1] == char
    second_occured = password[high-1] == char
    if first_occured and not second_occured or not first_occured and second_occured:
        valid_count_part_2 += 1

print(valid_count_part_1, valid_count_part_2)
