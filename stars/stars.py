# Part I - Create a function that takes a list of numbers and prints out *
# Part II - Modify function allowing a list containing integers and strings to be passed.
# When string is passed display first letter instead of *. you may use the .lower string method

def draw_stars(num_list):
    num = ""
    string = ""
    for val in num_list:
        if isinstance(val, int):
            num = "*" * val
            print num
        elif isinstance(val, str):
            first = val[0].lower()
            string = first * len(val)
            print string


draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])