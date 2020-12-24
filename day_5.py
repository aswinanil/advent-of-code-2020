file_handle = open('input_day_5.txt')
seats = file_handle.read().splitlines()

def locateSeat(pattern, start, end, start_char):
    for char in pattern:
        num_seats = end - start + 1

        if char == start_char:
            end -= num_seats/2
        else:
            start += num_seats/2

    return end

def getRowColumn(seat):
    row = locateSeat(seat[:-3], 0, 127, 'F')
    column = locateSeat(seat[-3:], 0, 7, 'L')
    return [row, column]

seat_ids = []
for seat in seats:
    [row, column] = getRowColumn(seat)
    seat_ids.append(row * 8 + column)

seat_ids = sorted(seat_ids)
print(seat_ids[-1])  # part 1

for i in range(len(seat_ids) - 1):
    if seat_ids[i+1] - seat_ids[i] > 1:
        print(seat_ids[i] + 1)  # part 2
