def drawGrid():
    for i in range(5):
        if i%2 == 0:
            # print(even)
            for j in range(5):
                if j%2 ==0:
                    print(" ",end="")
                else:
                    print("|",end="")
            print()        
                            
        else:
            print("_____")    
            
# drawGrid()      



Player = 1
gridKey = [[" "," "," "],[" "," "," "],[" "," "," "]]  #row by colum   

print(gridKey)

while(True):
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
        
    

    