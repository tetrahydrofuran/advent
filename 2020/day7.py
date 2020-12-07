import re


def parse_parent_containers(rule):
    parent, child = rule.split('contain')
    parent = re.sub(r'bags?', '', parent).strip()
    child = re.findall(r'[0-9]+ (\w+ \w+) bag', child)  # Ignores quantity
    return {parent: child}


def part1(rule_set, target='shiny gold'):
    all_rules = {}
    for r in rule_set:  # First-layer rule unpacking
        all_rules.update(parse_parent_containers(r))
    print(all_rules)
    qualifying = find_qualifying_wrapper_bags(target, all_rules)
    qualifying = set(qualifying)
    qualifying.remove(target)
    print(qualifying)
    return len(qualifying)


def find_qualifying_wrapper_bags(target, bag_dict):
    """Searches the bag dict recursively to find all parent bags that could contain the given target bag"""
    parents = [target]
    for k, v in bag_dict.items():
        # print(k, v, target in v)
        if target in v:
            parents += find_qualifying_wrapper_bags(k, bag_dict)
    return parents


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

    with open('files/7.txt') as f:
        input_ = f.readlines()
    rules = [i.strip() for i in input_]
    # print(parse_parent_containers(rules[0]))
    print(part1(rules))
