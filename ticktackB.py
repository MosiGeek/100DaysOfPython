def drawGrid(gkey):
    for row in range(5):
        if row % 2 == 0:
            val_row = int(row / 2)

            # print(even)
            for col in range(5):
                if col % 2 == 0:
                    val_col = int(col / 2)

                    print(gkey[val_col][val_row], end="")
                else:
                    print("|", end="")
            print()

        else:
            print("_____")
            

def check_winner(gKey):
    gridKey = gKey
    if (
        bool(gridKey[0][0] == gridKey[0][1] == gridKey[0][2])
        and (gridKey[0][0] == gridKey[0][1] == gridKey[0][2] != " ")
        or bool(gridKey[1][0] == gridKey[1][1] == gridKey[1][2])
        and (gridKey[1][0] == gridKey[1][1] == gridKey[1][2] != " ")
        or bool(gridKey[2][0] == gridKey[2][1] == gridKey[2][2])
        and (gridKey[2][0] == gridKey[2][1] == gridKey[2][2] != " ")
        or bool(gridKey[0][0] == gridKey[1][0] == gridKey[2][0])
        and (gridKey[0][0] == gridKey[1][0] == gridKey[2][0] != " ")
        or bool(gridKey[0][1] == gridKey[1][1] == gridKey[2][1])
        and (gridKey[0][1] == gridKey[1][1] == gridKey[2][1] != " ")
        or bool(gridKey[0][2] == gridKey[1][2] == gridKey[2][2])
        and (gridKey[0][2] == gridKey[1][2] == gridKey[2][2] != " ")
        or bool(gridKey[2][0] == gridKey[1][1] == gridKey[0][2])
        and (gridKey[2][0] == gridKey[1][1] == gridKey[0][2] != " ")
        or bool(gridKey[0][1] == gridKey[1][1] == gridKey[2][2])
        and (gridKey[0][1] == gridKey[1][1] == gridKey[2][2] != " ")
    ):
        print("Winnnnner !!")


Player = 1
gridKey = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]  # row by column

# print(gridKey)
drawGrid(gridKey)




while True:
    print(f"Current Player : {Player}")
    # check_winner(gridKey)

    row = int(input("Enter Row :"))
    col = int(input("Enter column :"))

    if gridKey[col][row] == " ":
        if Player == 1:
            gridKey[col][row] = "X"
            Player = 2
        else:
            gridKey[col][row] = "O"
            Player = 1

    # print(gridKey)
    drawGrid(gridKey)
    check_winner(gridKey)
