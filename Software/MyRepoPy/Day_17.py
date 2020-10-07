def fibonacci(a,b,n):
    if n>0:
        print (a+b)
        fibonacci(b,a+b,n-1)
        
a=int(input())
b=int(input())
n=int(input())
print("Fibonacci Series")
print (a)
print (b)
fibonacci(a,b,n)
h=input("Enter any key")