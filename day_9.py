import itertools
PRE_AMBLE_LENGTH = 25

# file_handle = open('input_day_9_example.txt')
file_handle = open('input_day_9.txt')
numbers = [int(line) for line in file_handle.read().splitlines()]

def is_sum_of_two_numbers(preamble, number):
    sums = []
    for (a, b) in list(itertools.combinations(preamble, 2)):
        sums.append(a + b)
    return number in list(set(sums))

for i in range(PRE_AMBLE_LENGTH, len(numbers)):
    preamble = numbers[i-PRE_AMBLE_LENGTH:i]
    number = numbers[i]
    if not is_sum_of_two_numbers(preamble, number):
        print(number)
        break
