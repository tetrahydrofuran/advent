def binary_partition(bin_str):
    # Probably not efficient, but eh.
    options = [i for i in range(2 ** (len(bin_str)))]

    for c in bin_str:
        ln = len(options)
        options = options[ln // 2:] if c in ('B', 'R') else options[:ln // 2]
    return options[0]


def part1(seats):
    return max(calculate_seat_ids(seats))


def calculate_seat_ids(seats):
    ids = []
    for seat in seats:
        seat = seat.strip()  # Keep forgetting to strip, sigh
        r = binary_partition(seat[:7])
        c = binary_partition(seat[7:])
        ids.append(r * 8 + c)

    return ids


def part2(seats):
    seats = sorted(calculate_seat_ids(seats))
    print(seats)
    for i, seat in enumerate(seats):
        if seat + 1 != seats[i + 1]:  # Should be +2
            return seat + 1  # My seat is +1


if __name__ == '__main__':
    with open('files/5.txt') as f:
        input_ = f.readlines()
    print(part1(input_))
    print(part2(input_))
