a=input('enter the string : ')
out=' '
for i in a:
    if i not in out:
        c=0
        for j in a:
            if j==i:
                c+=1
        out+=i+str(c)
print(out)
