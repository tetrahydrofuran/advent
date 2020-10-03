with open('files/1.txt') as f:
    input_ = f.read().strip()


def calculate_captcha1(captcha):
    counter = 0

    for i, digit in enumerate(captcha):
        try:  # Normal digit
            match = digit == captcha[i + 1]
            print(counter, digit, captcha[i + 1])

        except IndexError:  # Last digit, wrap to first
            match = digit == captcha[0]

        if match:
            counter += int(digit)
    return counter


def calculate_captcha2(captcha):
    # Split the list into 2, check equivalence.  Also only need to check one half, and double at the end.
    half = len(captcha) // 2
    a = captcha[:half]
    b = captcha[half:]
    return sum(2 * int(a[i]) for i in range(half) if a[i] == b[i])


if __name__ == '__main__':
    # Part 1
    assert calculate_captcha1('1122') == 3
    assert calculate_captcha1('1111') == 4
    assert calculate_captcha1('1234') == 0
    assert calculate_captcha1('91212129') == 9

    print('Part 1:', calculate_captcha1(input_))

    assert calculate_captcha2('1212') == 6
    assert calculate_captcha2('1221') == 0
    assert calculate_captcha2('123425') == 4
    assert calculate_captcha2('123123') == 12
    assert calculate_captcha2('12131415') == 4
    print('Part 2:', calculate_captcha2(input_))
