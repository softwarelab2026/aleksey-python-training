def main():
  print_nums()

def print_nums():
  for num in range(0, 101):
    if contains_seven(num) or num % 7 == 0:
      print(num, end=' ')

def contains_seven(num: int):
  while num > 0:
    if num % 10 == 7:
      return True
    num //= 10
  return False

if __name__ == '__main__':
  main()
