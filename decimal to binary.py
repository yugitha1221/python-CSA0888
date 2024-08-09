n=int(input("enter the vallue:"))
s=" "
while(n>0):
    r=n%2==0
    s=str(r)+s
    n=n//2
    print(s)
