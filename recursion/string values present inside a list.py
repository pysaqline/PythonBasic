
#while loop
'''a=[2,'hi',6.5,'hello','ram',89]
i=0
out=[]
while i<len(a):
    if type(a[i])==str:
        out+=[a[i]]
    i+=1
print(out)'''
#recursion condition same as while loop
'''def strg(a,i=0,out=[]):
    if i<len(a):
        if type(a[i])==str:
            out+=[a[i]]
        return strg(a,i+1,out)
    return out
print(strg([2,'hi',6.5,'hello','ram',89]))'''
#recursion condition reverse of while loop
'''def strg(n,i=0,out=[]):
    if i>=len(n):
        return out
    if type(n[i])==str:
        out+=[n[i]]
    return strg(n,i+1,out)
print(strg([2,'hi',6.5,'hello','ram',89]))'''

    
        

    
