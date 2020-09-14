def texto1(a):
  return f'{a} bugs no software, pegue um deles e conserte... \nTecle "Ctrl+F5" '
def texto2():
  return f'Vamos fazer mais um café!'
def main():
  for y in range(99, 251):
    bugs = texto1(y)
    print(f'{bugs}')
  print(f'{texto2()}')


if __name__=='__main__':
  main()    
