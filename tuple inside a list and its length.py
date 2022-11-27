#build a list of tuple with its name and len of the string

'''a='Work hard in silence and let the success make the noise'
l=[]
for word in a.split( ):
    t=()
    t+=word,len(word)
    l.append(t)
print(l)'''

#using comprehensions
a=input()
print([(word,len(word)) for word in a.split()])

