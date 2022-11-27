num=int(input('Enter the number : '))
'''num=float(input('Enter the number : '))
num=complex(input('Enter the number : '))'''
if type(num) in(int,float,complex):
    print('it,s a',type(num))
else:
    print('not a number')
