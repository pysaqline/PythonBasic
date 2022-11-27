#infinite loop statement
'''a=10
while True:
    print(a)'''
a=int(input('enter a no :'))
fac=1
if a==0:
    fac=0
while a>0:
    fac*=a
    a-=1
print(f'{}! =', fac)
    
