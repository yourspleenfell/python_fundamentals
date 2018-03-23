# Find Chracters - Write a program that takes a list of strings and a string containing a single character, and then prints a new list of all strings containing that character.

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

temp = [ ] # Sets a blank list as the variable 'temp'

for word in word_list:
    if char in word:
        temp.append(word) # Puts 'word' in varable 'temp'
print temp


