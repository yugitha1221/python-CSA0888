n=[2,4,5,7,9,1,4]
o_count=0
e_count=0
for i in n:
    if(i%2==0):
        e_count=e_count+i**2
    else:
        o_count=o_count+i**2
print(e_count)
print(o_count)
