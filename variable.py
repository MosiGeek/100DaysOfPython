# variables let you store and use information for later use

PI = 3.142343125
# one = 1
# two = 2
# three = 3

one, two, three = 1, 2, 3

print(one)
print(two)
print(three)

two = 4

print(two)
print(one)


decimal = 3.456
print(decimal)
StringVar = "This is a String"
print(StringVar)


# Global variables are not enclosed in any functions
print(PI)


def functionName():
    # global one
    print(one)
    # local variable
    newVar = "Hello World"
    print(newVar)
    return


functionName()
# print(newVar)


Eight = 5 + 3

print(Eight)

count = 9

# count = count + 1
count /= 3
# count *= 3
# count += 3
# count - = 3
print(count)
