# You need to write a function, that returns the first non-repeated character in the given string.

# If all the characters are unique, return the first character of the string.
# If there is no unique character, return None.

# You can assume, that the input string has always non-zero length.

# Examples
# "test"   returns "e"
# "teeter" returns "r"
# "trend"  returns "t" (all the characters are unique)
# "aabbcc" returns None (all the characters are repeated)

# for loop that counts how many times each character appears in the string
# for loop that finds the first non-repeated character in the string

# Function 1

def non_repeating(word):
    char_count = {}

    for char in word:
        char_count[char] = char_count.get(char, 0) + 1
        
    for char in word:
        if char_count[char] == 1:
            return char
    
    return None

print(non_repeating("test"))
print(non_repeating("teeter"))
print(non_repeating("trend"))
print(non_repeating("aabbcc"))
            
# Function 2

# def count(string):

#     for character in string.lower():
#         if string.count(character) == 1:
#             return character
#     return None
        
# print(non_repeating("test"))
# print(non_repeating("teeter"))
# print(non_repeating("trend"))
# print(non_repeating("aabbcc"))

# Function 3

# def non_repeating(word):
#     for char in word:
#         count = 0
#         for item in word:
#             if char == item:
#                 count += 1
#         if count == 1:
#             return char
#     return None

# print(non_repeating("test"))
# print(non_repeating("teeter"))
# print(non_repeating("trend"))
# print(non_repeating("aabbcc"))
