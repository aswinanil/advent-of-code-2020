file_handle = open('day_3_input.txt')
lines = file_handle.read().splitlines()

width = len(lines[0])
height = len(lines)

x = 3
y = 1
count_trees = 0

while y < height:
    if lines[y][x] == '#':
        count_trees+=1

    y+=1
    x+=3
    if x >= width:
        x-=width

print(count_trees)
