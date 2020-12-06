FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def get_passports(inputs):
    """Converts input into whole passports"""
    passports = []
    p = ''
    for line in inputs:
        if line == '\n':
            passports.append(p)
            p = ''
        else:
            p += line.replace('\n', ' ')
    passports.append(p)  # Catch the last block
    return passports


def part1(passports, optional=('cid',)):
    fields = FIELDS.copy()
    for i in optional:
        fields.remove(i)
    valid = 0
    for p in passports:
        valid += all((i in p for i in fields))
    return valid


def parse_passports(passports):
    parsed_passports = []
    for p in passports:
        parsed = {}
        p = p.strip().split(' ')
        for kv in p:
            key, value = kv.split(':')
            parsed[key] = value
        parsed_passports.append(parsed)
    return parsed_passports


def part2(parsed_passports):
    valid = 0
    for p in parsed_passports:
        try:
            conditions = [
                check_year(p['byr'], 1920, 2002),
                check_year(p['iyr'], 2010, 2020),
                check_year(p['eyr'], 2020, 2030),
                check_height(p['hgt']),
                check_hair(p['hcl']),
                p['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),  # Check eyes
                p['pid'].isnumeric() and len(p['pid']) == 9,  # Passport ID check
            ]
            # print(p)
            # print(conditions)
            valid += all(conditions)
        except KeyError:
            continue  # Missing field or failed to satisfy

    return valid


# region Checks
def check_year(value, miny, maxy):
    # Four-digit check is implicit from provided miny, maxy
    try:
        value = int(value)
        return miny <= value <= maxy
    except ValueError:
        return False


def check_height(height):
    try:
        if 'cm' == height[-2:]:
            height = int(height.replace('cm', ''))
            return 150 <= height <= 193
        elif 'in' == height[-2:]:
            height = int(height.replace('in', ''))
            return 59 <= height <= 76
    except ValueError:  # Not assuming all inputs are well-formed
        pass
    return False


def check_hair(hcl):
    if len(hcl) != 7 or hcl[0] != '#':
        return False
    hcl = hcl[1:]
    for ch in hcl:
        if not (48 <= ord(ch) <= 57 or 97 <= ord(ch) <= 102):  # 0-9, a-f
            return False
    return True


# endregion

if __name__ == '__main__':
    with open('files/4.txt') as f:
        input_ = f.readlines()

    pp = get_passports(input_)
    print(pp)
    print(part1(pp))
    pp = parse_passports(pp)
    print(part2(pp))
