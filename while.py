# while loop

# while (condition):
#     Action

# counter = 1
# number = 0

# while (counter <= 100):
#     number += 1
#     print(number,end="\t")
    
#     if number%2 == 0:
#         print("Even")
#     else:
#         print("Odd")

#     counter += 1


# counter = 1
# Sum = 0

# while (counter<=10):
#     Sum = Sum + counter
#     print(counter)
#     counter+=1

# print("***************************************************")
# print(Sum)


letters = ["a","b","c","d"]

# printing the list using the for loop
# for letter in letters:
#     print(letter)

# printing the list using the while loop
# counter = 0

# while counter < len(letters):
#     print(letters[counter])
#     counter += 1
    
height = 5000
speed = 50
time = 0

while(height>0):
    height = height - speed
    print(height,end="\t")
    time = time + 1
    print(time)
    

print("********************************")
print(height,end="\t")
print(time)