def prime(x):
    z=0
    if x>1:
        for i in range(2,x):
            if x%i == 0:
                return 0
                z=1
        if z==0:
            return 1

a = int (input ("Enter a beginning number"))
b = int (input ("Enter a ending number")) 
                   
for i in range(a,b+1):
    if prime(i):
        print ("{} ".format(i))

ch = input("Press any key to exit")        