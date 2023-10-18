# # use functions if you wanna ddo things over and over

# # def nameOfFunction(Input):
# #     #Action
# #     return Output


# def addOne(number):
#     number += 1
#     return number


# val = 0

# output = addOne(val)

# kout = addOne(5.8)
# print(output)
# print(kout)


def addOneAddTwo(numOne, numTwo):
    result = numOne + 1

    result += result + numTwo
    # result = result + result + 2
    return result


out = addOneAddTwo(3, 4)
print(out)
