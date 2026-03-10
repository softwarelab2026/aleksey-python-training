def main():
  print_nums_from_one_to_six()

def print_nums_from_one_to_six():
  for i in range(10, 51, 10):
    for j in range(i-9,i):
      print(round(j*0.1,2), end=' ')
    print(int(i*0.1))


if __name__ == '__main__':
  main()
