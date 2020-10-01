#Quadratic Equation Program
import cmath

a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Emter c:"))

d=(b*b)-(4*a*c)

res1= (-b - cmath.sqrt(d))/(2*a)
res2= (-b + cmath.sqrt(d))/(2*a)

print("Delta=",d)
print("The roots of the equation are")
print(res1)
print(res2)
