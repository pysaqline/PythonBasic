'''Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place
of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR".'''
age=int(input('enter the age : '))
sex=input('sex(M OR F) : ')
if sex=='f':
    print('she will work only in urban areas')
elif sex=='m':
    marital_status=input('marital status ( Y or N ) : ')
    if 20<=age<=40 and marital_status=='Y' :
        print('anywhere')
    elif 40<=age<=60:
        print('urban area')
else:
    print('error')
    
