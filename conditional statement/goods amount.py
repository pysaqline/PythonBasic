good=int(input('Enter the quantity: '))
if good*100>1000:
    print('U need to pay : ',(good*100)-((good*100)*.10))
else:
    print('U need to pay : ',good*100)
