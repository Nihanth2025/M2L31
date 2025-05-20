y1=float(input("Enter the number1: "))
x2=float(input("Enter the number2: "))

while x2 !=0:
    z=x2
    x2=y1 % x2
    y1=z

HCF=y1
print("HCF= ",HCF)