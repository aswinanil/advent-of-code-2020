file_handle = open('input/input_day_7.txt')
lines = file_handle.read().splitlines()
bags = []
for line in lines:
    [outer_bag, inner_bags] = line.split(' contain ')
    inner_bags = inner_bags[:-1].split(', ')
    bags.append([outer_bag, inner_bags])

def parse_bag_color(inner_bag):
    [inner_bag_num, inner_bag_color] = inner_bag.split(' ', 1)
    return inner_bag_color.rsplit(' ', 1)[0]

def parse_bag_color_and_count(inner_bag):
    [inner_bag_num, inner_bag_color] = inner_bag.split(' ', 1)
    inner_bag_num = int(inner_bag_num) if inner_bag_num != 'no' else 0
    return (inner_bag_num, inner_bag_color.rsplit(' ', 1)[0])


# Part 1
def does_contain_inner_bag_color(inner_bags, target_inner_bag_color):
    for inner_bag in inner_bags:
        inner_bag_color = parse_bag_color(inner_bag)
        if inner_bag_color == target_inner_bag_color:
            return True

def get_outer_bag_colors(inner_bag_color):
    outer_bag_colors = []
    for bag in bags:
        if does_contain_inner_bag_color(bag[1], inner_bag_color):
            outer_bag_colors.append(bag[0].rsplit(' ', 1)[0])

    return outer_bag_colors

gold_bag_heirarchy = [['shiny gold']]
while len(gold_bag_heirarchy[-1]):
    next_level = []
    for bag_color in gold_bag_heirarchy[-1]:
        next_level.extend(get_outer_bag_colors(bag_color))
    gold_bag_heirarchy.append(list(set(next_level)))

flatten = lambda t: [item for sublist in t for item in sublist]
print(len(set(flatten(gold_bag_heirarchy[1:]))))


# Part 2
def populate_inner_bags(outer_bag):
    inner_bags = []
    for bag in bags:
        if bag[0].rsplit(' ', 1)[0] == outer_bag.color:
            inner_bags = [parse_bag_color_and_count(inner_bag) for inner_bag in bag[1]]

    for [count, color] in inner_bags:
        if color == 'other':
            break
        outer_bag.add_child(Node(count, color))

class Node(object):
    def __init__(self, count, color):
        self.count = count
        self.color = color
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
        obj.parent = self
        obj.total_count = obj.count * self.total_count

gold_bag = Node(1, 'shiny gold')
gold_bag.total_count = 1
populate_inner_bags(gold_bag)
current_depth_children = gold_bag.children
inner_count = 0

while len(current_depth_children) > 0:
    for bag in current_depth_children:
        inner_count += bag.total_count
        populate_inner_bags(bag)

    current_depth_children = flatten([child.children for child in current_depth_children])

print(inner_count)
