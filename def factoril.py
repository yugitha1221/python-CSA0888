def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("entno:"))
result=fact(n)
print(result)
    
