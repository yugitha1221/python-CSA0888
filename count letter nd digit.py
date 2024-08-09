def count_l_d(s):
    l=0
    d=0
    for char in s:
        if char.isalpha():
            l=l+1
        elif char.isdigit():
            d=d+1
    return l,d
s="helo123"
l,d=count_l_d(s)
print(l,d)
    
