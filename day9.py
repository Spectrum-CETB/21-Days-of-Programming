n=int(input("enter the number: "))
sum_=0
for i in range(1,n):
    if(n%i)==0:
        if(i%2)!=0:
            sum_=sum_+i
print(sum_)        
