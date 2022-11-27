'''write a program to check the given list collection is having exact middle value
or not if it is having exact middle value then check whether the middle value is integer
or not ,if it is an integer print the value'''
a=[10,20,True,'hello',3,85,7.6,3+5j,99]
if len(a)%2==1:
    mid=len(a)//2
    if type(mid)==int:
        print(a[mid])
    else:
        print('not an int')
else:
    print('does not have middle value')
