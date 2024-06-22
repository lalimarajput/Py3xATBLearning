#Anagram of string:-
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase


def are_anagrams(s1, s2):
    # Remove spaces (if any) and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Check if lengths are different
    if len(s1) != len(s2):   #if length of s1 is not equals to s2, return False
        return False

    # Sort characters in both strings and compare
    return sorted(s1) == sorted(s2)


# Test cases
s1 = "silent"
s2 = "listen"
print(f"Are '{s1}' and '{s2}' anagrams? {are_anagrams(s1, s2)}")  # Output: Are 'silent' and 'listen' anagrams? True

s3 = "hello"
s4 = "world"
print(f"Are '{s3}' and '{s4}' anagrams? {are_anagrams(s3, s4)}")
# Output: Are 'hello' and 'world' anagrams? False
# because no phrase is formed by rearranging the words

s1 = "namo"
s2 = "onam"
print(f"Are '{s1}' and '{s2}' anagrams? {are_anagrams(s1, s2)}")  # Output: Are 'namo' and 'onam' anagrams? True
