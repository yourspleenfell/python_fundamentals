words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
newwords = words.replace( "day", "month")
print newwords

x = [2, 54, -2, 7, 12, 98]
print max(x)
print min(x)
x.insert(0, "hello")
x.append("world")

print x[0]
print x[-1]

for i in x:
    if i == x[0]:
        newx = [i]
    if i == x[-1]:
        newx.append(i)
print newx

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()
xx = [x[0:5]]
xx.extend(x[5:12])

print xx

# first_half = [ ]
# second_half = [ ]

# for index in range(0, 11):
#     if index < 5:
#         first_half.append(x[index])
#     else:
#         second_half.append(x[index])

# first_half.extend(second_half)

# print first_half