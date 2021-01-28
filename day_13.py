file_handle = open('input/input_day_13.txt')
[earliest_timing, bus_services] = file_handle.read().splitlines()

# Part 1
earliest_timing = int(earliest_timing)
bus_services_without_x = list(filter(lambda a: a != 'x', bus_services.split(',')))
bus_services_without_x = [int(bus_service) for bus_service in bus_services_without_x]

def get_bus_timing(bus_service):
    earliest_bus_iteration = earliest_timing / bus_service

    if earliest_bus_iteration % 1 != 0:
        earliest_bus_iteration = int(earliest_bus_iteration) + 1

    return earliest_bus_iteration * bus_service

bus_timings = [(bus_service, get_bus_timing(bus_service)) for bus_service in bus_services_without_x]

[earliest_bus, earliest_bus_timing] = bus_timings[0]
for i in range(1, len(bus_timings)):
    (bus, timing) = bus_timings[i]
    if timing < earliest_bus_timing:
        earliest_bus_timing = timing
        earliest_bus = bus

print((earliest_bus_timing - earliest_timing) * earliest_bus)


# Part 2
bus_services = bus_services.split(',')
first_bus_interval = int(bus_services[0])
first_bus_timing = 0

first_multiplier = 0
multiplier_interval = 1
highest_pattern_count = 0
first_multiplier_dict = {}
multiplier_interval_dict = {}

pattern_found = False
while not pattern_found:
    first_bus_timing += first_bus_interval * multiplier_interval

    next_timing = first_bus_timing
    pattern_found = True
    pattern_count = 0

    for bus in bus_services[1:]:
        next_timing += 1

        if bus == 'x':
            continue
        else:
            bus = int(bus)
            if next_timing % bus == 0:
                pattern_count += 1

                if pattern_count > highest_pattern_count:
                    highest_pattern_count = pattern_count

                    if not pattern_count in first_multiplier_dict:
                        first_multiplier_dict[pattern_count] = first_bus_timing / first_bus_interval

                elif pattern_count == highest_pattern_count and pattern_count not in multiplier_interval_dict:
                    multiplier_interval = first_bus_timing / first_bus_interval - first_multiplier_dict[pattern_count]
                    multiplier_interval_dict[pattern_count] = multiplier_interval

                continue
            else:
                pattern_found = False
                break

    if pattern_found:
        print(first_bus_timing)
