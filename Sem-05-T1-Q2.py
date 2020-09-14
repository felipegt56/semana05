def main():
  par = 0
  impa = 0
  for n in range(100):
    num = int(input('Digite um número: '))
    if (num % 2) == 0:
      par += 1
    else:
      impa += 1
  print(f'{par}')
  print(f'{impa}')

if __name__=='__main__':
  main()
