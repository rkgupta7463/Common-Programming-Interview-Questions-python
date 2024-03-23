## How do you calculate the number of numerical digits in a string?

strings="jiuytfghvb78455erfejgf324gtrnhtnhjn5645wrefdbhj65774ght54"

c=0
for  i in strings: 
    if i.isdigit():
        c+=1

print(f"number of numerical:- {c}")