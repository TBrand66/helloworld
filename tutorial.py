## Augumented assigned operator

x = 10
x -= 3
x += 4
print(x)

#####
x = 10 + 3 * 2**2
print(x)

## built-in round function
x = 2.9
print(round(x))

# absolute function - returns positive value of a number
x = 3.9
print(abs(-3.9))

## math module
### serach python 3 math modules on google
import math

print(math.ceil(2.9))
print(math.floor(2.9))

if statement

is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")

price = 1000000
Good_credit = True

if Good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")


name = input('pass: ')
if int(name) <= 3:
    print("name must be at least 3 characters")
elif int(name) > 50:
    print("name can be a maximum of 50 cahracters")
else:
    print("name looks good")



name = input("name: ")
if len(name) <= 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good")

## weight converter

weight = input('weight: ')
unit = input("(L)bs or (k)g: ")
if unit.upper() == "L":
    converted = int(weight) * 0.45
    print(f"You are {converted} kilos")
else:
    converted = int(weight) / 0.45
    print(f"You are {converted} kg")
