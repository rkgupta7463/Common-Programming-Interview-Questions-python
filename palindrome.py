## How do you determine if a string is a palindrome?
## Answer: The term derives from the Greek palin dromo (“running back again”). Examples of word palindromes include “civic,” “madam,” “radar,” and “deified.”  

string="civic" ## civic is palindrome string and abcd is not palindrome 

rev=string[::-1]  # reverse the

if rev==string:
    print("String palindrome")
else:
    print("Not")