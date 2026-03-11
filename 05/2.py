def factorial(target_num: int) -> int:
  result = 1
  for i in range(target_num,0,-1):
    result *= i
  return result

def append_beep_to_string(s: str) -> str:
  return s+'beep'

def mul_2nums(num1, num2):
  result = num1 * num2
  if result < 0: return 0
  else: return result

def main():
  print('{}!={}'.format(1, factorial(1)))
  print('{}!={}'.format(4, factorial(4)))
  print('{}!={}'.format(5, factorial(5)))
  print('s={} --> {}'.format('Hello', append_beep_to_string('Hello')))
  print('{}*{}={}'.format(2, 4, mul_2nums(2, 4)))
  print('{}*{}={}'.format(-1, 3, mul_2nums(-1, 3)))

if __name__ == '__main__':
  main()
