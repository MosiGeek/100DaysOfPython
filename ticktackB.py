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


# function to check whether the values of the horizontal, vetical, diagonal axis are equal, if equal then return winner
def check_winner(gKey, turn):
    gridKey = gKey
    # winning_player = str(turn.pop())
    winning_player = str(turn)
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
        or bool(gridKey[0][0] == gridKey[1][1] == gridKey[2][2])
        and (gridKey[0][0] == gridKey[1][1] == gridKey[2][2] != " ")
    ):
        # print(f"*** Player {winning_player} WIIIIIINNS !!!*** GAME OVER")
        return "W"
        
    elif (
        gridKey[0][0] != " "
        and gridKey[0][1] != " "
        and gridKey[0][2] != " "
        and gridKey[1][0] != " "
        and gridKey[1][1] != " "
        and gridKey[1][2] != " "
        and gridKey[2][0] != " "
        and gridKey[2][1] != " "
        and gridKey[2][2] != " "
    ):
        # print("DRAAAAAAAAAWW!!!")
        return "D"
        


Player = 1
gridKey = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]  # row by column
turn = []

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
            turn.append(Player)
            Player = 2

        else:
            gridKey[col][row] = "O"
            turn.append(Player)
            Player = 1

    # print(gridKey)
    drawGrid(gridKey)
    
    if check_winner(gridKey, turn) == "W":
        print(check_winner(gridKey,turn))
        break
    elif check_winner(gridKey, turn) == "D":
        break
    
