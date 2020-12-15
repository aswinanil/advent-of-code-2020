file_handle = open('day_1_input.txt')
expenses_string = file_handle.readlines()
expenses = [int(i) for i in expenses_string]

for i in range(0, len(expenses)-1):
    for j in range(i+1, len(expenses)-1):
        if (expenses[i] + expenses[j] == 2020):
            print(expenses[i] * expenses[j])
