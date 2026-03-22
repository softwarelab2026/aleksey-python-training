def two_step_slice(list1: list) -> list:
  return list1[::2]

def main():
  list1 = [1, 2, 3, 4, 5]
  print(f"list1: {list1}")
  print(f"result: {two_step_slice(list1)}")

if __name__ == '__main__':
  main()
