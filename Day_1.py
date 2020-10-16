a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
d=b**2-(4*a*c)
print(d)
if(d<0):
    print('('"-"+str(b)+"+"+str(int(abs(d)**0.5))+"i"+')'+"/"+str(2*a))
    print('('"-"+str(b)+"-"+str(int(abs(d)**0.5))+"i"+')'+"/"+str(2*a))
else:
    print((-b+(d**0.5))/2*a)
    print((-b-(d**0.5))/2*a)
