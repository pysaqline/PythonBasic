''' WAP to check whether the user credentials is matching with the stored usernname
and password or not.If it is matching only username than print invalid password
if it is mactching both username and password print login successfull.If it is not matching username than directly print
user not found.'''
user='saqline'
pswd='123@'
userin=input('enter the username : ')
pswdin=input('enter the pswd : ')
if userin==user:
    if pswdin==pswd:
        print('login successful')
    else:
        print('invalid password')
else:
    print('user not found')
