#Pattern In Python
n=int(input("Enter the num of rows:"))

print("The Pattern:")

for i in range(65,65+n):
    n=n-1
    for j in range(n,0,-1):
        print(" ",end=" ")
    for k in range(65,i+1):
        print(chr(k),end=" ")
    for l in reversed(range(65,i)):
        print(chr(l),end=" ")
    print()
