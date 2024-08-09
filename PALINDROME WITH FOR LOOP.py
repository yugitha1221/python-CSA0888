A="MADAM"
REV=""
for i in range(len(A)-1,-1,-1):
    REV+=A[i]
print(REV)
if REV==A:
    print("it is palindrome")
else:
    print("not")
