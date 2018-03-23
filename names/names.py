# Part I
# def names():
#     students = [
#         {'first_name':'Michael', 'last_name':'Jordan'},
#         {'first_name':'John', 'last_name':'Rosales'},
#         {'first_name':'Mark', 'last_name':'Guillen'},
#         {'first_name':'KB', 'last_name':'Tonel'},
#     ]
#     for data in students:
#             print data["first_name"] + " " + data["last_name"]

# names()

#Part II
def layered_names():
    users = {
        'Students': [
            {'first_name' :  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ],
        'Instructors': [
            {'first_name' : 'Michael', 'last_name' : 'Choi'},
            {'first_name' : 'Martin', 'last_name' : 'Puryear'}
        ]
    }
    num = 0
    for key, data in users.items():
        print key
        for k, d in enumerate(data, 1):
            num = len(d["first_name"]) + len(d["last_name"])
            print str(k) + " - " + d["first_name"].upper() + " " + d["last_name"].upper() + " - " + str(num)

layered_names()