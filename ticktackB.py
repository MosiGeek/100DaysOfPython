# possible_val = [
#     [["X", "O", "X"], [" ", "X", "O"], ["X", "O", " "]],
#     [["X", "O", "X"], [" ", "O", "X"], ["O", "X", " "]],
#     [["X", "O", "X"], ["X", "O", " "], [" ", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", " ", "O"]],
#     [["X", "O", "X"], ["O", "X", "X"], ["X", " ", "O"]],
#     [["X", "O", "X"], ["X", "O", "O"], ["O", "X", " "]],
#     [["X", "O", "X"], ["X", "O", " "], [" ", "O", "X"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", " ", "O"]],
#     [["X", "O", "X"], ["O", "X", "X"], ["X", "O", " "]],
#     [["X", "O", "X"], ["O", "X", " "], [" ", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", " ", "O"]],
#     [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", " ", "X"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "X", "O"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "O", "X"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "X", "O"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "O", "X"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "X", "O"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "O", "X"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "X", "O"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "O", "X"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "X", "O"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "O", "X"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "X", "O"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "O", "X"]],
#     [["X", "O", "X"], [" ", "O", "X"], ["X", "O", "X"]],
#     [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]],
#     [["X", "O", "X"], ["O", "X", " "], ["X", "X", "O"]],
# ]

# with open("possible.txt","w") as possible:
#     for val in possible_val:
#         possible.write(str(val)+"\n")
#     print("Done")


def drawGrid():
    for i in range(5):
        if i % 2 == 0:
            # print(even)
            for j in range(5):
                if j % 2 == 0:
                    print(" ", end="")
                else:
                    print("|", end="")
            print()

        else:
            print("_____")


drawGrid()


Player = 1
gridKey = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]  # row by column

print(gridKey)

while True:
    if Player == 1:
        print(f"Current Player - {Player}")

        row = int(input("Enter Row :"))
        col = int(input("Enter column :"))

        gridKey[row][col] = "X"

        print(gridKey)
        Player = 2
    else:
        print(f"Current Player {Player}")

        row = int(input("Enter Row :"))
        col = int(input("Enter Col :"))

        gridKey[row][col] = "O"

        print(gridKey)
        Player = 1


# counter = 0
# while counter <= 2:
#     for i in gridKey[counter]:
#         print(i, end=" ")
#     print("\n")
#     counter += 1
