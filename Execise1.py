Length = 5
character = "o"
for pos in range(1,Length+1):
    #print(-pos)
    print(character*pos)

# use step to direct the loop which way to count
for inner in range(Length-1,0,-1):
    print(character*inner)