print("enter quantity")
quan=int(input())
if quan*100>1000:
    print ("cost is",((quan*100)-(.1*quan*100)))
else:
    print ("cost is",quantity*100)
