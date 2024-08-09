def addition(a,b):
    sum=a+b
    return sum
def subtraction(a,b):
    sum=a-b
    return sub
a=int(input("enter value a:"))
b=int(input("enter the value b:"))
p=(input("enter the value p:"))
if(p=="+"):
    result=addition(a,b)
    print(result)
elif (p=="-"):
    result=subtraction(a,b)
    print(result)
else:
    print("enter the vaild op:")
    
