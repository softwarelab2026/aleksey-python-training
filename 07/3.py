def is_valid_input(user_input: str) -> bool:
    return user_input.isdigit() and len(user_input) == 5

def list_digits(num: int) -> str:
    num = abs(num)
    digits = []
    power = count_digits(num)-1
    while power >= 0:
        digit = (num // (10 ** power)) % 10
        digits.append(str(digit))
        power -= 1
    return ', '.join(digits)

def count_digits(num: int) -> int:
    num = abs(num); count = 0
    if num == 0:
        return 1

    while num > 0:
        count += 1
        num //= 10
    return count

def sum_digits(num: int) -> int:
    num = abs(num)
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum

def main():
    num = None
    while True:
        user_input = input("Please, provide a five digit number: ")
        if is_valid_input(user_input):
            num = int(user_input)
            break

    print(num)
    print(list_digits(num))
    print(sum_digits(num))

def tests():
    assert is_valid_input('12345')
    assert not is_valid_input('1234')
    assert not is_valid_input('hello')
    assert list_digits(12345) == '1, 2, 3, 4, 5'
    assert count_digits(12345) == 5
    assert sum_digits(12345) == 15

if __name__ == '__main__':
    tests()
    main()
