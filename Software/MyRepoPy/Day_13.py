def prime(n):
    bru = 0
    for i in range (2,n):
        if n % i == 0:
            bru = 1
            break
    if bru == 0 or n == 1:
        return 1
    else:
        return 0
def primebig(k):
    for i in range(1,k):
        if k % i == 0:
            if prime(i):
                t = i
    return t

k = int(input("Enter a number from 1 to 1015 to get its largest prime factor:"))
print (primebig(k))      