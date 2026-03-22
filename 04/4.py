def main():
  num = int(input('Please enter a 5 digit number\n'))
  print('You entered the number: {}'.format(num))
  print('The digits of this number are:' + list_digits(num))
  print('The sum of this digits is:' + sum_digits(num))


def list_digits(num: int) -> str:
  result = ''
  power = count_digits(num)-1
  while power >= 0:
    result += f"{num // 10 ** power % 10}, "
    power -= 1
  result += str(num % 10)
  return result


def count_digits(num: int):
  count = 0
  while num >= 0:
    count += 1
    num //= 10
  return count

def sum_digits(num: int):
  sum_dig = 0
  while num > 0:
    sum_dig += num % 10
    num //= 10
  return sum_dig

if __name__ == '__main__':
  main()
