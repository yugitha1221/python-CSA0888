n=int(input("enter the value:"))
d=0
for i in range(1,n+1):
    if(n%i==0):
        d=d+i
if(d>2):
    print("composite")
else:
    print("not")
