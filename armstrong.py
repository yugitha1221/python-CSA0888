n=153
sum=0
d=(int(digit)for digit in str(n))
for i in d:
    sum=sum+i**3
if(sum==n):
    print("it is armstrong")
else:
    print("not")
