# Checkerboard - Write a program that prints a 'checkerboard' pattern to the console.

for val in range(0,8): # Loops while 'val' is in the range of 0-7
    if val%2 == 0:
        print "* * * * " # Prints this if number divisble by 2
    else:
        print " * * * *" # Prints this if number not divisible by 2