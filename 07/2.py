def list_is_nums(input_list: list) -> bool:
    for element in input_list:
        if not element.isdigit(): return False
    return True

def main():
    assert (list_is_nums([])) is False
    assert (list_is_nums(1, 2, 3, 4, 5)) is True
    assert (list_is_nums(1, 2.5, 228)) is True
    assert (list_is_nums(2, 'hello', 3)) is False
    assert (list_is_nums(1, False, 3)) is True
if __name__ == '__main__':
    main()
