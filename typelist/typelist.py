# Type List - Write a program that takes a list and prints a message for each element in the list, based on that element's data type.abs
# If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

def typeList(x):
    nums = [ ]
    string = "String:"
    data = [False,False]
    for value in x:
        if isinstance(value, int) or isinstance(value, float):
            nums.append(value)
            data[0] = True
        else:
            string += " " + value         
            data[1] = True
    
    if all(data):
        print "The array you entered is of mixed type"
        print string
        print "Sum:", sum(nums)
    elif data[1]:
        print "The array you entered is of string type"
        print string
    elif data[0]:
        print "The array you entered is of integer type"
        print "Sum: ", sum(nums)

typeList(['Harry Potter', 54, "wand", 20, -34, "Hogwarts", 6.54, 3.14])