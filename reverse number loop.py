n=int(input("enter the no:"))
rev_no=0
while n!=0:
    lastd=n%10
    rev_no=rev_no*10+lastd
    n=n//10
print(rev_no)
