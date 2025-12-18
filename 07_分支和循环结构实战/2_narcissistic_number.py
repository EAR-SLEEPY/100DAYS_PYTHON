for i in range(100,1000):
    hundred=i//100
#    print(hundred)
    ten=i%100//10
#    print(ten)
    sig=i%10
#   print(sig)
    if hundred**3+ten**3+sig**3==i:
        print(f'{i}')