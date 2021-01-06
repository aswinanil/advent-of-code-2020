import pdb

# file_handle = open('input_day_15_example.txt')
file_handle = open('input_day_15.txt')
[numbers] = [[int(num) for num in line.split(',')] for line in file_handle.read().splitlines()]

def speak_number(turn):
    global turn_sequences, last_spoken_number

    if last_spoken_number not in turn_sequences:
        last_spoken_number = 0
        turn_sequences[0] = [turn]
    elif len(turn_sequences[last_spoken_number]) == 1:
        last_spoken_number = 0
        turn_sequences[0].append(turn)
    else:
        last_spoken_number = turn_sequences[last_spoken_number][-1] - turn_sequences[last_spoken_number][-2]
        if last_spoken_number not in turn_sequences:
            turn_sequences[last_spoken_number] = [turn]
        else:
            turn_sequences[last_spoken_number].append(turn)

turn_sequences = {}

for i in range(len(numbers)):
    turn_sequences[numbers[i]] = [i+1]
last_spoken_number = numbers[-1]

for i in range(len(numbers), 2020):
    speak_number(i+1)

print(last_spoken_number)
