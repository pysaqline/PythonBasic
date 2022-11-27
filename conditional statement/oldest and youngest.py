a=int(input('enter 1st age : '))
b=int(input('enter 2nd age : '))
c=int(input('enter 3rd age : '))
if a>b and a>c:
    print(' oldest is', a)
elif c>a and c>b:
    print('Oldest is : ', c)
elif b>a and b>c:
    print('oldest  is : ',b)
else:
    print('all are equal')
