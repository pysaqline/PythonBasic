'''def armstrong(n):
    a=str(n)
    out=0
    for i in a:
        out+=int(i)**len(a)
    if out==n:
        print('armstrong number')
    else:
        print('not armstrong')
    
armstrong(int(input('enter the number')))'''
#type 2 function
'''def occ(a):
    out=''
    for i in a:
        if i not in out:
            c=0
            for j in a:
                if i==j:
                    c+=1
            out+=i+str(c)
    print(out)
occ('ssssddddpppffff')'''
#type 3 function
'''def occ():
    a='ffffhhhhkkk'
    out=''
    for i in a:
        if i not in out:
            c=0
            for j in a:
                if j==i:
                    c+=1
            out+=i+str(c)
    return(out)
print(occ())'''
#type 4 function
def occ(a):
    out=''
    for i in a:
        if i not in out:
            c=0
            for j in a:
                if i==j:
                    c+=1
            out+=i+str(c)
    return(out)
print(occ('aabbbccddd'))

























                    
