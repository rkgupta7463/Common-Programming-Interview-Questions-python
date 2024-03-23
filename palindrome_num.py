## How do you determine if a number is a palindrome?

num=121

rev=0
temp=num
while num>0:
    digit = num%10
    rev = rev*10 + digit
    num //= 10
    
if temp == rev:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")