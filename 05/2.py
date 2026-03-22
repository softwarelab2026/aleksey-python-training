def factorial(target_num: int) -> int:
  result = 1
  for i in range(1, target_num):
    result *= i
  result *= target_num
  return result

def append_beep_to_string(s: str) -> str:
  return s+'beep'

def mul_2nums(num1: int, num2: int) -> int:
  result = num1 * num2
  if result < 0: return 0
  else: return result

def main():
  print(f"{1}!={factorial(1)}")
  print(f"{4}!={factorial(4)}")
  print(f'{5}!={factorial(5)}')
  print(f"s={'Hello'} --> {append_beep_to_string('Hello')}")
  print(f"{2}*{4}={mul_2nums(2, 4)}")
  print(f"{-1}*{3}={mul_2nums(-1, 3)}")

if __name__ == '__main__':
  main()
