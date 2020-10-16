n = list(input("Enter a list of numbers here: "))
temp = n[0]
n[0] = n[-1]
n[-1] = temp
print(n)
input("Enter any key to exit")