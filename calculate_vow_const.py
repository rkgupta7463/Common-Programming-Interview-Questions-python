## How do you calculate the number of vowels and consonants in a string?

strings="dfghbfvcasfeAEUefgvb"

vowel=['a','e','i','o','u','A','E','I','O','U']

v=0
c=0 

for s in range(len(strings)):   
    if strings[s] in vowel:
        v+=1
    else:
        c+=1

print(f"number of vowels are {v} and number of consonants are {c}")