file_handle = open('input/input_day_3.txt')
lines = file_handle.read().splitlines()

width = len(lines[0])
height = len(lines)

def get_count (x_traversal, y_traversal):
    count_trees = 0
    x=0
    y=0

    while y < height:
        if lines[y][x] == '#':
            count_trees+=1

        y += y_traversal
        x += x_traversal
        if x >= width:
            x-=width

    return count_trees

# part 1
print(get_count(3, 1))

# part 2
product = 1
for (x, y) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    product *= get_count(x, y)

print(product)
