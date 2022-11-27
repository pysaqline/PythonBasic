#while loop
'''n=int(input('enter a number : '))
i=1
s=1
out=[]
while i<=n:
    s*=i
    out+=[s]
    i+=1
if n in out:
    j=1
    su=0
    while j<n:
        if n%j==0:
            su+=j
        j+=1
    if su==n:
        print('perfect factorial number')
    else:
        print('not perfect fac no')'''
#using for loop
'''n=int(input('enter a number : '))
i=1
s=1
out=[]
while i<=n:
    s*=i
    out+=[s]
    i+=1
if n in out:
    su=0
    for j in range(1,n):
        if n%j==0:
            su+=j
    if su==n:
        print('perfect fac no')
    else:
        print('not perfect fac')'''
#using recursion
def fac(n,i=1,p=1,out=[]):
    if i<=n:
        p*=i
        out+=[p]
        return fac(n,i+1,p,out)
    return out
def perfect(n,i=1,s=0):
    if i<n:
        if n%i==0:
            s+=i
        return perfect(n,i+1,s)
    if s==n and n in fac(n):
        return True
    else:
        return False
print(perfect(int(input('enter a no: '))))



















        
        
        
        














