def perfect(a):
    out=[]
    for i in a:
        s=0
        for j in range(1,i):
            if i%j==0:
                s+=j
        if s==i:
            out.append(i)
    return out
print(perfect([2,3,4,6,18,28]))
