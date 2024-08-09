n=[4,54,29,71,7,59,98,23]
primecount=0
compositecount=0
for num in n:
    if num>1:
        d=0
        for i in range(2,num):
            if num%i==0:
                d+=1
        if d>0:
            compositecount+=1
        else:
            primecount+=1
print(primecount)
print(compositecount)
        
