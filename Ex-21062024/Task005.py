#String reverse:-

# 1. Using Slicing
def reverse_string_slicing(s):
    return s[::-1]  #slicing

print(reverse_string_slicing("lalima"))  # Output: "amilal"

# 2. Using the reversed() Function and join()

def reverse_string_reversed(s):
    return ''.join(reversed(s))

print(reverse_string_reversed("lalima"))  # Output: "amilal"

# 3. Using loop

def reverse_string_loop(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string_loop("lalima"))  # Output: "amilal"