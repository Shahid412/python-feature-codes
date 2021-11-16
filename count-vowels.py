# string of vowels
vowels = 'aeiou'

# change this value for a different result
_str = 'Hello, is this anchor from dabian city?'

# uncomment to take input from the user
#_str = input("Enter a string: ")

# make it suitable for caseless comparisions
_str = _str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in _str:
   if char in count:
       count[char] += 1

print(count)

