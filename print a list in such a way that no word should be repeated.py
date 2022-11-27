#print a list in such a way that no word should be repeated

a=['hi','hello','hi','hello','in','hi']
l=[]
for word in a:
    if word not in l:
        l.append(word)
print(l)

#print([word for word in a if word not in l ])


