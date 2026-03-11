def main():
  sentence = input('Enter your sentence:\n')
  result = encrypt_text(sentence)
  print(result)

def encrypt_text(string: str) -> str:
  result = ''
  for char in string:
    result += char
    if char in ('a','e','i','o','u'):
      result += 'b' + char
  return result

if __name__ == '__main__':
  main()
