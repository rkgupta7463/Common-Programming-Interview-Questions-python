## How do you find the non-matching characters in a string?

strings1="hello"
strings2="hallo"

non_match_char=[]

if len(strings1)==len(strings2):
    for s in range(len(strings1)):
        if  strings1[s]!=strings2[s]:
            non_match_char.append(strings1[s])
            non_match_char.append(strings2[s])
else:
    print("Strings are not of equal length")

print("Non matching characters are: ",non_match_char)