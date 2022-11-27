d={}
alph=['vowels','consonents']
v=[]
c=[]
for asci in range(ord('a'),ord('z')+1):
    if chr(asci) in ('aeiou'):
        v.append(chr(asci))
        d.update({alph[0]:len(v)})
    else:
        c.append(chr(asci))
        d.update({alph[1]:len(c)})
print(d)
