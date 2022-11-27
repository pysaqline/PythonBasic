a=int(input('enter number of classes held : '))
b=int(input('enter number of classes attended : '))
atten = (b/a)*100
if atten>75:
    print('allowed to sit for exam')
else:
    print('not allowed to sit for exam')
