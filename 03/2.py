def main():
  var1, var2 = 0, 1
  print(var1, end=' ')
  print(var2, end=' ')
  while True:
    sum1 = var1 + var2
    if sum1 >= 10000:
      break
    print(sum1, end=' ')
    var1 = var2
    var2 = sum1



if __name__ == '__main__':
  main()
