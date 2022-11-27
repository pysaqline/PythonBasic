#this is by extracting value in for loop and for knowing the index we need to specify
#varname.index(i)
def string(a):
    out=[]
    for i in a:
        if a.index(i)%2==0 and type(i)==str and len(i)>=2 and 'h' in i:
            out.append(i)
    return out
print(string(['gi','hello','valo','kamon','acho','tumi','harun']))


#for extracting index by range function we use
#range(len(varname))
def string(a):
    out=[]
    for i in range(len(a)):
        if i%2==0 and type(a[i])==str and len(a[i])>=2 and 'h' in a[i]:
            out.append(a[i])
    return out
print(string(['gi','hello','valo','kamon','acho','tumi','harun']))


