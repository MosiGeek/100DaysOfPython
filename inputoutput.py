# I/O in python

# Var = input("Message to the user")

# name = input("Whats your name: \n")

# print(name)

# age = int(input("whats your age? :"))


# print(str(age)+"1")


listOfNums = []
avg = 0
print(listOfNums)

for i in range(5):
    val = int(input(f"Gimme an interger-{str(i)} :"))
    listOfNums.append(val)

# average score 
for i in range(len(listOfNums)):
    avg += listOfNums[i]

print(f"Average of {avg} given {len(listOfNums)} Numbers is : {round(avg/len(listOfNums))}")

