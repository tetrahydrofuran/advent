import re


def part1(rule_set, target='shiny gold'):
    all_rules = {}
    for r in rule_set:  # First-layer rule unpacking
        all_rules.update(parse_parent_containers(r))
    # print(all_rules)
    qualifying = find_qualifying_wrapper_bags(target, all_rules)
    qualifying = set(qualifying)
    qualifying.remove(target)
    # print(qualifying)
    return len(qualifying)


def parse_parent_containers(rule):
    parent, child = rule.split('contain')
    parent = re.sub(r'bags?', '', parent).strip()
    child = re.findall(r'[0-9]+ (\w+ \w+) bag', child)  # Ignores quantity
    return {parent: child}


def find_qualifying_wrapper_bags(target, bag_dict):
    """Searches the bag dict recursively to find all parent bags that could contain the given target bag"""
    parents = [target]
    for k, v in bag_dict.items():
        # print(k, v, target in v)
        if target in v:
            parents += find_qualifying_wrapper_bags(k, bag_dict)
    return parents


def part2(rule_set, target='shiny gold'):
    all_rules = {}
    for r in rule_set:  # First-layer rule unpacking
        all_rules.update(parse_parent_containers_with_quantity(r))
    # print(all_rules)
    return get_bags_contained(target, all_rules)


def parse_parent_containers_with_quantity(rule):
    """Unpacks rule line into {parent: [(quantity, bag) for bag in children]}"""
    parent, child = rule.split('contain')
    parent = re.sub(r'bags?', '', parent).strip()
    child = re.findall(r'([0-9]+) (\w+ \w+) bag', child)  # Ignores quantity
    return {parent: child}


def get_bags_contained(target, bag_dict):
    """Recursively goes down the bag container dict to get the quantity of bags contained within"""
    children = 0
    for bag in bag_dict[target]:
        x = get_bags_contained(bag[1], bag_dict)
        # print(target, bag_dict[target], bag[0], x)
        children += int(bag[0]) * (x + 1)  # +1 for self
    return children


if __name__ == '__main__':
    test_rules = '''
    light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''.strip().split('\n')

    test_rules2 = '''
    shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
    '''.strip().split('\n')

    with open('files/7.txt') as f:
        input_ = f.readlines()
    rules = [i.strip() for i in input_]
    # print(parse_parent_containers_with_quantity(test_rules[0]))
    print('Part 1:', part1(rules))
    print('Part 2:', part2(rules))
