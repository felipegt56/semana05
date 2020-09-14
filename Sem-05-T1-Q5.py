def texto(a):
  return f'{a} bugs no software, pegue um deles e conserte...'

def main():
  for a in range(99, 251):
    bugs = texto(a)
    print(f'{bugs}')

if __name__=='__main__':
  main()    
