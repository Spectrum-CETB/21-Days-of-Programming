s = int(input("Input any number of your Choice: "))
sum = 0
for num in range(1,s+1):
    x = s%num
    if x == 0:
       
        if num % 2 != 0:
            sum += num
print(sum)
ch = input("Enter any key to exit")