def prestacao(x, y):
  return f'{x}x de R$ {y:.2f}'

def calculo( a, b):
  return (a / b)

def main():
  compra = float(input())
  for p in range(1, 25):
    pagamento = calculo(compra, p)
    prestacao1= prestacao(p, pagamento)
    print(f'{prestacao1}')


if __name__=='__main__':
  main()
