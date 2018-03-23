# Create a dictionary containing information about yourself. Keys should include name, age, country of birth and favorite language.
# Write a function that will print something about the dictionary.

def aboutMe():
    me = {
        "first_name":"Dylan",
        "last_name":"Arbuthnot",
        "age":"26",
        "birthplace":"Phoenix, AZ, USA",
        "fav_lang":"Python!"
    }
    for val in me.itervalues():
        if val == me["first_name"]:
            print "My first name is " + val
        elif val == me["last_name"]:
            print "My last name is " + val
        elif val == me["age"]:
            print "I am " + val + " years old"
        elif val == me["birthplace"]:
            print "I was born in " + val
        elif val == me["fav_lang"]:
            print "My favorite language is " + val

aboutMe()