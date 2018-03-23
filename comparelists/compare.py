# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.
# If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same."

def listCompare (list_one, list_two):
    data = [False, False] # Makes a boolean list with both values defaulted to false
    if list_one == list_two:
        data[0] = True
    else:
        data[1] = True
    
    if data[0]: # Executes if index of 0 in data is set to true
        print "The lists are the same"
    elif data[1]: # Executes if index of 1 in data is set to true
        print "The lists are not the same"

listCompare(['celery','carrots','bread','creampie'], ['celery','carrots','bread','cream'])