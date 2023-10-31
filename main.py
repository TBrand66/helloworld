# name = input ("what is your name? ")
# best_colour = input ('what is your best colour? ')
# print (name + ' likes ' + best_colour)


# weight = input('weight: ')
# print (0.4535 * int(weight))

# weight_lbs = input('weight: ')
# weight_kg = float(weight_lbs) * 0.45
# print (weight_kg)

# course = """
# hi john
# thank you for this opportunities
# forever in your dept
# """
# print (course)

# course = 'python for beginners'
# print (course[1:-1])

### formated strings

first = 'john'
last = 'Smith'
message = (first + ' [' + last +
           '] is a coder')
msg = f'{first} [{last}] is a coder'
print(msg)

course = 'python for beginner'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('o'))
print(course.replace('beginner', 'Absolute beginner'))
