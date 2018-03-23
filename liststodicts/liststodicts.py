name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "red pandas", "jellyfish"]

def make_dict(list1, list2):
    if len(list1) > len(list2):
        new_dict = zip(list1,list2)
    else:
        new_dict = zip(list2,list1)
    # print zip_list
    # print len(list1), len(list2)
    return new_dict

make_dict(name, favorite_animal)