n=4
p=[]
num=2
while len(p)<n:
    sumofno=0
    for i in range(1,num):
        if num%i==0:
            sumofno=sumofno+i
    if(sumofno==num):
        p.append(num)
        num=+1
print(p)
