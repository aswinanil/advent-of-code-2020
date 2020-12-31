# file_handle = open('input_day_10_example_2.txt')
file_handle = open('input_day_10.txt')
jolts = [int(line) for line in file_handle.read().splitlines()]

jolts.sort()
count_1 = 0
count_3 = 0

def increment(jolt_diff):
    global count_1, count_3

    if jolt_diff == 1:
        count_1 += 1
    elif jolt_diff == 3:
        count_3 += 1

increment(jolts[0])
for i in range (len(jolts)-1):
    increment(jolts[i+1] - jolts[i])

count_3 += 1
print(count_1 * count_3)
