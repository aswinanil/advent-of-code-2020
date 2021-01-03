import pdb

# file_handle = open('input_day_13_example.txt')
file_handle = open('input_day_13.txt')
[earliest_timing, bus_services] = file_handle.read().splitlines()
earliest_timing = int(earliest_timing)
bus_services = list(filter(lambda a: a != 'x', bus_services.split(',')))
bus_services = [int(bus_service) for bus_service in bus_services]

def get_bus_timing(bus_service):
    earliest_bus_iteration = earliest_timing / bus_service

    if earliest_bus_iteration % 1 != 0:
        earliest_bus_iteration = int(earliest_bus_iteration) + 1

    return earliest_bus_iteration * bus_service

bus_timings = [(bus_service, get_bus_timing(bus_service)) for bus_service in bus_services]

[earliest_bus, earliest_bus_timing] = bus_timings[0]
for i in range(1, len(bus_timings)):
    (bus, timing) = bus_timings[i]
    if timing < earliest_bus_timing:
        earliest_bus_timing = timing
        earliest_bus = bus

print((earliest_bus_timing - earliest_timing) * earliest_bus)
