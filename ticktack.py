row=" "
col="|"

for i in range(5):
    if i%2 == 0:
        # print("  |  |  ")
        for j in range(5):
            if j%2 == 0:
                if j != 4:
                    print(row,end="")
                else:
                    print(row)
            else:
                print(col,end="")    
    else:
        print("_____")
 