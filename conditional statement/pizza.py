menu={'cheeseloaded':120,'vegloaded':180,'chickenloaded':240}
addon={'extracheese':20,'ketchup':30}

a=input('enter the flavour : ')
quan=int(input('enter the quantity : '))
b=input('press 1 if u need a addon : ')
bill=0
if a in menu:
    bill=bill+menu[a]*quan
    if b=='1':
        c=input('enter the addon : ')
        if c in addon:
            bill = bill + addon[c]
            print('price = ' ,bill)
        else:
            print('add on not found : ')
    else:
        print('price = ',bill)
else:
    print('item not found')
