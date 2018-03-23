# Create a program called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whet it's and odd or even number.

# odd_even
def odd_even():
    for count in range(20):
        if count%2 == 0:
            print "Number is " + str(count) + ". This is an even number."
        else:
            print "Number is " + str(count) + ". This is an odd number."

odd_even()

# Multiply - Create a function called 'multiple' that iterates through each value in a list and returns a list where each value has been multipled by 5.

# multiply
def multiply(arr, num):
    for x in range(len(arr)):
        arr[x] *= num
    # print arr
    return arr

multiply([2, 4, 5], 3)

def layered_multiply(arr):
    new_arr = [ ]
    for x in range(len(arr)):
        new_arr.append([1] * arr[x])
    # print new_arr
    return new_arr

x = layered_multiply(multiply([2, 4, 5], 3))
print x