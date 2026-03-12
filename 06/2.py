def summer(list1):
  result = list1[0]
  for elem in list1[1:]:
    result+=elem
  return result

def main():
  print(f"{[10, 11, 12, 0.75]} -> {summer([10, 11, 12, 0.75])}")
  print(f"{[True, False, True, True]} -> {summer([True, False, True, True])}")
  print(f"{['aa', 'bb', 'cc']} -> {summer(['aa', 'bb', 'cc'])}")
  print(f"{[[1, 2, 3, 'a'], [4, 'b', 'c', 'd']]} -> {summer([[1, 2, 3, 'a'], [4, 'b', 'c', 'd']])}")

if __name__ in '__main__':
  main()
