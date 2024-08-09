decimal_no=int(input("enter the no:"))
binary_no=" "
octal_no=" "
decimalforoctal=decimal_no
while decimal_no>0:
    remainder=decimal_no%2
    binary_no=str(remainder)+binary_no
    decimal_no=decimal_no//2
    
while decimalforoctal>0:
    remainder=decimalforoctal%8
    octal_no=str(remainder)+octal_no
    decimalforoctal=decimalforoctal//8
print("the binaryno:",binary_no)
print("the octalno:",octal_no)
