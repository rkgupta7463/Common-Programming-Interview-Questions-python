## Write a logic to get the sum of first 'N' prime numbers

# Initialize the sum variable to 0
sum_val = 0
# Initialize the count variable to 0
count = 0
# Initialize the number variable to 2 (the first prime number)
num = 2
n=3

# Loop until the count reaches N
while count < n:

    # Check if the number is prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        # If the number is prime, add it to the sum and increment the count
        sum_val += num
        count += 1

    # Increment the number
    num += 1

# Print the sum of the first N prime numbers
print(sum_val)