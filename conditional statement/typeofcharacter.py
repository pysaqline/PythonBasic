char=input('Enter the character : ')
if 'A'<=char<='Z':
    print("it's an uppercase")
elif 'a'<=char<='z':
    print("it's an lowercase")
elif '0'<=char<='9':
    print("it's a numberic character")
else:
    print("it's an special character")
