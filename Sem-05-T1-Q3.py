def mil():
   return f'1000.'

def main():
    for a in range(10, 1000 , 10):
        print(a ,end=', ')
    print(mil())

if __name__=='__main__':
    main()
