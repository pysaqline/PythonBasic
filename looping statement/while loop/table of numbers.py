#while program to print the table of 24,50 and 29
#while loop
'''n=int(input('enter the no : '))
i=1
while i<=10:
    print(f'{n} * {i} =',n*i)
    i+=1'''
#for loop
'''n=20
for i in range(1,11):
    print(f'{n} * {i} =',n*i)'''
#function with no parameter no return
'''def mul():
    n=int(input('enter the no : '))
    for i in range(1,11):
        print(f'{n} * {i} =',n*i)
mul()'''
#function with parameter and return  (did not get the output)
#recursion reverse
def mul(n,i=1):
    if i>10:
        return('done')
    print(f'{n} * {i} =',n*i)
    return mul(n,i+1)
print(mul(int(input('enter the number'))))
#recursion condition same as while loop
def mul(n,i=1):
    if i<10:
        print(f'{n} * {i} =',n*i)
        return mul(n,i+1)
    return('Thank you')
print(mul(int(input('enter the number'))))

        
        
    
    
    
    
