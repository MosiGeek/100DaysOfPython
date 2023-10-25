row="_"
col="|"

for i in range(5):
    if i%2 == 0:
        # print("  |  |  ")
        for j in range(5):
            if j%2 == 0:
                print("  ",end="\t")
            else:
                print("|",end="")    
    else:
        print("________")
 