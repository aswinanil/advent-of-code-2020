file_handle = open('input_day_10.txt')
jolts = [int(line) for line in file_handle.read().splitlines()]
jolts.sort()

#  part 1
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


# Part 2
class Node(object):
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

adapter_compatible_jolts_hash = {}
def get_compatible_jolts(adapter):
    if adapter.index in adapter_compatible_jolts_hash:
        return adapter_compatible_jolts_hash[adapter.index]

    compatible_jolts = []
    i = adapter.index + 1

    while i < len(jolts) and jolts[i] - adapter.value < 4:
        compatible_jolts.append((jolts[i], i))
        i += 1

    adapter_compatible_jolts_hash[adapter.index] = compatible_jolts
    return compatible_jolts

distinct_ways_count = 0
distinct_ways_hash= {}
def populate_children(parent):
    global distinct_ways_count

    compatible_jolts = get_compatible_jolts(parent)
    for (jolt, index) in compatible_jolts:
        parent.add_child(Node(jolt, index))

    if len(parent.children) == 0:
        distinct_ways_count += 1

    if parent.index in distinct_ways_hash:
        distinct_ways_count += distinct_ways_hash[parent.index]
    else:
        parent.starting_distinct_ways_count = distinct_ways_count
        for child in parent.children:
            populate_children(child)
        distinct_ways_hash[parent.index] = distinct_ways_count - parent.starting_distinct_ways_count

outlet = Node(0, -1)
populate_children(outlet)
print(distinct_ways_count)
