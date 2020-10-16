mc = input("Enter your Secret Code")
c=0
for i in mc:
    if i == " ":
        print (chr(ord(i)),end = "" )
        c=0
    elif c%2 == 0:
        print (chr(ord(i)-1),end = "" )
        c+=1
    elif c%2 == 1:
        print (chr(ord(i)+1),end = "" )
        c+=1
print("")
m = input("Enter any key")