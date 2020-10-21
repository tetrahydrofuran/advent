import hashlib


def hash_hex(key: str, number: int) -> int:
    return hashlib.md5('{}{}'.format(key, number).encode('utf-8')).hexdigest()


def find_smallest_satisfying_hash(key, hash):
    """Iterates through each number, stopping when the hash begins with specified"""
    i = 0
    hash_head = ''
    while hash_head != hash:
        hash_head = str(hash_hex(key, i))[:len(hash)]
        i += 1

    return i - 1  # Get rid of final addition


def part1(key: str) -> int:
    """Stop when hash begins with 00000"""
    return find_smallest_satisfying_hash(key, '00000')


def part2(key: str) -> int:
    """Copy of part1, modifying the check to be 6x0"""
    return find_smallest_satisfying_hash(key, '000000')


if __name__ == '__main__':
    # noinspection SpellCheckingInspection
    input_ = 'yzbqklnj'

    # assert part1('abcdef') == 609043
    print(part1(input_))
    print(part2(input_))
