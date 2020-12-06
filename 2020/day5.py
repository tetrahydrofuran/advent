def binary_partition(binstr):
    # Probably not effecient, but eh.
    options = [i for i in range(2 ** (len(binstr)))]

    for c in binstr:
        ln = len(options)
        options = options[ln // 2:] if c in ('B', 'R') else options[:ln // 2]
    return options[0]


def part1(seats):
    max_id = 0
    for seat in seats:
        seat = seat.strip()  # Keep forgetting to strip, sigh
        r = binary_partition(seat[:7])
        c = binary_partition(seat[7:])
        print('{} | {}, {} | {}'.format(seat, r, c, r * 8 + c))
        max_id = max(max_id, r * 8 + c)
    return max_id


if __name__ == '__main__':
    with open('files/5.txt') as f:
        input_ = f.readlines()
    print(part1(input_))
