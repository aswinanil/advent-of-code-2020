file_handle = open('input_day_6.txt')
groups = file_handle.read().split('\n\n')
groups[-1] = groups[-1][:-1]  # end of file newline

def getUnanimousAnswerCount(individuals):
    result = set(individuals[0])
    for individual in individuals:
        result = result.intersection(set(individual))
        if len(result) == 0:
            return 0
    return len(result)

count = 0
unanimous_count = 0
for group in groups:
    # part 1
    unique_answers = set(group.replace('\n', ''))
    count += len(unique_answers)

    # part 2
    individuals = group.split('\n')
    unanimous_count += getUnanimousAnswerCount(individuals)

print(count)
print(unanimous_count)
