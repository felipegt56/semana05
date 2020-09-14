def frase(a):
  return f'{a} bugs no software, pegue sete deles e conserte... \nTecle "Ctrl+F5" '
def texto():
  return f'Vamos fazer mais um café!'
def main():
  for y in range(99, 251, 7):
    a = frase(y)
    print(f'{a}')
  print(f'{texto()}')


if __name__=='__main__':
  main()    
