file_handle = open('input_day_4.txt')
lines = file_handle.read().split('\n\n')
lines = [line.replace('\n', ' ') for line in lines]
lines[-1] = lines[-1][:-1]  # end of file newline

passports = [line.split(' ') for line in lines]

passports_parsed = []
for passport in passports:
    passport_dict = {}

    for field in passport:
        [key, value] = field.split(':')
        passport_dict[key] = value

    passports_parsed.append(passport_dict)

def fields_are_valid(passport):
    byr = passport['byr']
    if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
        return False

    iyr = passport['iyr']
    if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
        return False

    eyr = passport['eyr']
    if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
        return False

    hgt = int(passport['hgt'][:-2])
    unit = passport['hgt'][-2:]
    if unit == 'cm' and (hgt < 150 or hgt > 193):
        return False
    elif unit == 'in' and (hgt < 59 or hgt > 76):
        return False
    elif unit != 'cm' and unit != 'in':
        return False

    hcl = passport['hcl']
    if hcl[0] != '#':
        return
    hcl = hcl[1:]
    if len(hcl) != 6:
        return
    for char in hcl:
        if char not in ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return False

    if passport['ecl'] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    pid = passport['pid']
    if len(pid) != 9 or not pid.isdigit():
        return False

    return True

all_fields_present_count = 0
valid_count = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in passports_parsed:
    all_fields_present = True
    for field in required_fields:
        if field not in passport:
            all_fields_present = False
            break

    if all_fields_present:
        all_fields_present_count+=1  # part 1

        if fields_are_valid(passport):
            valid_count+=1  # part 2

print(all_fields_present_count)
print(valid_count)
