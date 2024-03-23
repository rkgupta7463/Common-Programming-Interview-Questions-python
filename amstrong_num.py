## ## How do you determine if a number is a amstrong number?

num=153

temp=num
s=0

while num>0:
    digit=num%10
    s+=digit*digit*digit
    num//=10

if temp==s:
    print(f"{temp} is an Armstrong number")
else:
    print(f"{temp} is not an Armstrong number")