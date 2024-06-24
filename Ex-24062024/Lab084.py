letters=['a','b','c','d','e','i','j','o']
#filter vowels(a,e,i,o,u)

def vowel(letter):
    vowels=['a','e','i','o','u']
    return letter in vowels

result=filter(vowel,letters)
print(list(result))    #gives [a,e,i,o] in list

result=vowel('p')
print(result)  #gives False, because p is not vowel