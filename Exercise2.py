# Exercise 2 lists and dictiionaries Exercise



BlackShoes = {
    42:2,
    41:3,
    40:4,
    39:1,
    38:0
}

while(True):
    purchaseSize = int(input("Which shoe size would you like to buy? :\n"))
    
    if BlackShoes[purchaseSize] in BlackShoes:
        BlackShoes[purchaseSize] -= 1
    else:
        print("nothing here")
        break