# def drawGrid(gkey):
#     for row in range(5):
#         if row % 2 == 0:
#             val_row = int(row/2)
            
#             # print(even)
#             for col in range(5):
#                 if col % 2 == 0:
#                     val_col = int(col/2)
                    
#                     print(gkey[val_col][val_row], end="")
#                 else:
#                     print("|", end="")
#             print()

#         else:
#             print("_____")


# Player = 1
# gridKey = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]  # row by column

# print(gridKey)
# drawGrid(gridKey)

# while True:
    
#     print(f"Current Player : {Player}")

#     row = int(input("Enter Row :"))
#     col = int(input("Enter column :"))
    
    
#     if gridKey[col][row] == " ":
        
#         if Player == 1:
#             gridKey[col][row] = "X"
#             Player = 2
#         else:
            
#             gridKey[col][row] = "O"
#             Player = 1
        
#     print(gridKey)
#     drawGrid(gridKey)




# # counter = 0
# # while counter <= 2:
# #     for i in gridKey[counter]:
# #         print(i, end=" ")
# #     print("\n")
# #     counter += 1


# checking if a player has won                 
# check if a certain row or column has the same type e.g x or o
# what if i use a function that will text the gridKey for every row/column and return True if winner or Draw if there is no winner 

gridKey = [["X", "X", "O"], ["O", "X", "X"], ["X", "X", "O"]]

# check = bool(gridKey[0][1] == gridKey[1][1] == gridKey[1][2])

# print(gridKey[0][1])
# print(gridKey[1][1])
# print(gridKey[1][2])

# print(check)


