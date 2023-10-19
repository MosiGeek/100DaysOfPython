# Lists

scores = [70,85,51,67.5,90]

# get length of the list
# print(len(scores))


# for i in range (0,len(scores)):
#     print(scores[i])

# to the get the last element in the list
# print(scores[-1])
# print(scores[-5])

# in human speek: go from zero(0) upto but not including two (2)
print(scores[0:2])

# changing the values in a list

scores[0] = 77
# lists can hold any values that is numbers,text or other lists
# scores[4] = "hello"

print(f"{scores},length is {len(scores)}")

# erasing values in a list
# scores[1:4] = []
# print(scores)


# putting values at the end of the list - appending to a list

scores.append(40)

print(f"{scores},length is {len(scores)}")