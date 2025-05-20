num=int(input("Enter the number: "))
r=0

t=num
while t>0:
    x=t % 10
    r=x + (r*10)
    t=int(t/10)

if r==num:
    print(num,"is Palindrome number")

else:
    print(num,"is not a Palindrome number")