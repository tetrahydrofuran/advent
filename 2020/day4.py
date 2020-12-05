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
    return passports


def part1(passports, optional=('cid',)):
    fields = FIELDS.copy()
    for i in optional:
        fields.remove(i)
    valid = 0
    for p in passports:
        valid += all((i in p for i in fields))
    return valid


if __name__ == '__main__':
    with open('files/4.txt') as f:
        input_ = f.readlines()

    pp = get_passports(input_)
    print(part1(pp))
