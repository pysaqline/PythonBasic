#whie for perfect number
'''n=int(input('enter a no : '))
i=1
s=0
while i<n:
    if n%i==0:
        s+=i
    i+=1
if s==n:
    print(bool(1))
else:
    print(bool(0))'''
#recursion reverse
def perfect(n,i=1,s=0):
    if i>n:
        return(bool(0))
    if n%i==0:
        s+=i
    return perfect(n,i+1,s)
    if s==n:
        return(bool(1))
print(perfect(int(input('enter a number : '))))
'''def perfect(n,i=1,s=0):
    if i<n:
        if n%i==0:
            s+=i
        return perfect(n,i+1,s)
    if s==n:
        return(bool(1))
    else:
        return(bool(0))
print(perfect(int(input('enter a number : '))))'''


    
        

    
