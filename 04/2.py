def main():
  sentence = input('Enter your sentence:\n')
  result = encrypt_text(sentence)
  print(result)

def encrypt_text(s: str) -> str:
  res = ''
  for ch in s:
    res += ch
    if ch in ('a','e','i','o','u'):
      res += 'b' + ch
  return res

if __name__ == '__main__':
  main()
