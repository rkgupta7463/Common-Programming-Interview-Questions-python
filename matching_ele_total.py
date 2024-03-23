## How do you total all of the matching integer elements in an array?

num=[1,2,3,4,5,5,2,3,1]

total_ele=[]
for n in range(len(num)):
    for  m in range(n+1, len(num)):
        if num[m] == num[n]:
            total_ele.append(num[n])
            print("{0} and {1} are equal".format(num[n], num[m]))

print("The sum is: ",sum(total_ele)) 