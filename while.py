# while loop

# while (condition):
#     Action

counter = 1
number = 0

while counter < 100:
    number += 1
    print(number,end="\t")
    
    if number%2 == 0:
        print("Even")
    else:
        print("Odd")

    counter += 1


