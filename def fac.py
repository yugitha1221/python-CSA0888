n=int(input("enter the no"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
        print("is it")
else:
    print("not")
    
