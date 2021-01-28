import itertools
PRE_AMBLE_LENGTH = 25

file_handle = open('input/input_day_9.txt')
numbers = [int(line) for line in file_handle.read().splitlines()]

def is_sum_of_two_numbers(preamble, number):
    sums = []
    for (a, b) in list(itertools.combinations(preamble, 2)):
        sums.append(a + b)
    return number in list(set(sums))

# Part 1
num_not_sum_prev_25 = -1
for i in range(PRE_AMBLE_LENGTH, len(numbers)):
    preamble = numbers[i-PRE_AMBLE_LENGTH:i]
    number = numbers[i]
    if not is_sum_of_two_numbers(preamble, number):
        num_not_sum_prev_25 = number
        print(number)
        break


# Part 2
for i in range(len(numbers)):
    sum_contiguous = numbers[i]

    j = i+1
    while j < len(numbers) and sum_contiguous < num_not_sum_prev_25:
        contiguous_set_found = False
        sum_contiguous += numbers[j]

        if sum_contiguous == num_not_sum_prev_25:
            contiguous_set_found = True
            break;
        j+=1

    if contiguous_set_found:
        break;

contiguous_set = numbers[i:j+1]
print(min(contiguous_set) + max(contiguous_set))
