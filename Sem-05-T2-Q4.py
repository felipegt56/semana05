def texto(a):
  return f'{a} bugs no software, pegue onze deles e conserte... \nTecle "Ctrl+F5" '
def texto_1():
  return f'Sem erros no software! Está estabilizado!'
def main():
  for y in range(99, 0, -11):
    bugs = texto(y)
    print(f'{bugs}')
  print(f'{texto_1()}')


if __name__=='__main__':
  main()    
