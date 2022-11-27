n=int(input('enter a no : '))
i=1
s=0
while i<n:
    if n%i==0:
        s+=i
    i+=1
if s==n:
    print(bool(1))
else:
    print(bool(0))