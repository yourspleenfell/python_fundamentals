# # Multiples Part I - Write code that prints all odd numbers from 1 to 1000. Use the for loop and don't use a list

for i in range(1000): # states that we are looking for the value of 'i' in a range of 1000
    if i%2 != 0: # says if 'i' divided by 2 does not have a remainder of 0, indicating that it cannot be cleanly divided by 2
        print i # then we print 'i'

# # Multiples Part II - Create another program that prints all multiples of 5 from 5 to 1,000,000

for i in range (5, 1000000): # states that we are looking for the value of 'i' in a range of 5 - 1,000,000
    if i%5 == 0: # this says that if i can be divided by 5 and have a remainder of 0
        print i # we will print i

# Sum list - Create a program that prints the sum of all values in the list

a = [1, 2, 5, 10, 255, 3]

print sum(a) # prints the sum of the values in list 'a'

# Average List - Create a program that prints the average of the values in the list

print sum(a) / len(a) # sums the value in list 'a' and divides them by the length of list 'a' then prints the result
