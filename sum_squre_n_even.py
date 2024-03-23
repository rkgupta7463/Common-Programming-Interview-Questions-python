## Write a logic to get the sum of the squares of first 'N' even numbers
n=int(input("Enter number\n"))
s=0
for i in range(1,n+1):
    even_no=2*i
    if even_no%2==0:
        s+=even_no**2

print(s)