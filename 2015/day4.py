import hashlib


def hash_hex(key: str, number: int) -> int:
    return hashlib.md5('{}{}'.format(key, number).encode('utf-8')).hexdigest()


def part1(key: str) -> int:
    i = 0
    hash_head = ''
    while hash_head != '00000':
        hash_head = str(hash_hex(key, i))[:5]
        i += 1

    return i - 1  # Get rid of final addition


if __name__ == '__main__':
    # noinspection SpellCheckingInspection
    input_ = 'yzbqklnj'

    assert part1('abcdef') == 609043
    print(part1(input_))
