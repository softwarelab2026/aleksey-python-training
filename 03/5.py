def main():
  print_nums_from_zero_dot_one_to_five()

def print_nums_from_zero_dot_one_to_five():
  for i in range(0, 50, 10):
    for j in range(i+1, i+10):
      print(j/10, end=' ')
    print((i+10)//10)

if __name__ == '__main__':
  main()
