## How do you find out if the two given strings are anagrams?

str1="cat" # listen
str2="act" # silent

if sorted(str1)==sorted(str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")