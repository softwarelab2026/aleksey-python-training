def multiply(multiplicand, multiplier):
  return multiplicand*multiplier

def divide(dividend, divisor):
  if divisor == 0: return 'illegal'
  else: return dividend // divisor

def main():
  print('{}*{}={}'.format(2,3,multiply(2, 3)))
  print('{}//{}={}'.format(8,4,divide(8,4)))

if __name__ == '__main__':
  main()
