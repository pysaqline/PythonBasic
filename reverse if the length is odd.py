'''a=input()
l=[]
for word in a.split():
    if len(word)%2==0:
        l.append(word)
    else:
        l.append(word[::-1])
print(l)'''

#even word and count as well odd word and its count
a=input()
'''d={}
e=[]
o=[]
for word in a.split():
    if len(word)%2==0:
        e.append(word)
        d.update({'even word':len(e)})
    else:
        o.append(word)
        d.update({'odd word':len(o)})
print(d)'''

print([word if len(word)%2==0 else (word[::-1]) for word in a.split()])
