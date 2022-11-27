'''A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
Modify the above question to allow student to sit if he/she has medical cause.
Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.'''

a=int(input('enter number of classes held : '))
b=int(input('enter number of classes attended : '))
atten=(b/a)*100
if atten<75:
    medical=input('do u have a medical issue: ')
    if medical=='Y':
        print('allowed to sit for exam')
    elif medical=='N':
        print("not allowed to sit for exam")
else:
    print('allowed to sit for exam')
    


