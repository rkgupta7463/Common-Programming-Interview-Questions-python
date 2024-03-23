## Write a logic to get the sum of first 'N' prime numbers

n=int(input("Enter the value of N:"))

for i in range(2,n):
    if n%i!=0:
        print("prime number")
        break
    elif n>=1:
        print("not")
        break