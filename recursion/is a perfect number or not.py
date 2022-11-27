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
#same condition as while loop
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
#recursion reverse of perfect 
'''def rec(n,i=1,s=0):
    if i>n:
        return(bool(0))
    if s==n:
        return(bool(1))
    if n%i==0:
        s+=i
    return rec(n,i+1,s)
print(rec(int(input('enter a number : '))))'''



    
        

    
