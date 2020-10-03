with open('files/1.txt') as f:
    input_ = f.read().strip()


def calculate_captcha(captcha):
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


if __name__ == '__main__':
    # Part 1
    assert calculate_captcha('1122') == 3
    assert calculate_captcha('1111') == 4
    assert calculate_captcha('1234') == 0
    assert calculate_captcha('91212129') == 9

    print('Part 1:', calculate_captcha(input_))
