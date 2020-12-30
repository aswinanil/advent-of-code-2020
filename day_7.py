import pdb

# file_handle = open('input_day_7_example.txt')
file_handle = open('input_day_7.txt')
lines = file_handle.read().splitlines()
bags = []
for line in lines:
    [outer_bag, inner_bags] = line.split(' contain ')
    inner_bags = inner_bags[:-1].split(', ')
    bags.append([outer_bag, inner_bags])

def parse_bag_color(inner_bag):
    [inner_bag_num, inner_bag_color] = inner_bag.split(' ', 1)
    return inner_bag_color.rsplit(' ', 1)[0]

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
