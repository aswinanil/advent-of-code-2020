file_handle = open('input_day_1.txt')
expenses_string = file_handle.readlines()
expenses = [int(i) for i in expenses_string]

last_index = len(expenses) - 1

# part 1
for i in range(0, last_index):
    for j in range(i+1, last_index):
        if (expenses[i] + expenses[j] == 2020):
            print(expenses[i] * expenses[j])

        # part 2
        for k in range(j+1, last_index):
            if (expenses[i] + expenses[j] + expenses[k] == 2020):
                print(expenses[i] * expenses[j] * expenses[k])
