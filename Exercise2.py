# Exercise 2 lists and dictiionaries Exercise

# Examplee a shoe company that is using a dictionary to keep count of shoes in stock


BlackShoes = {42: 2, 41: 3, 40: 4, 39: 1, 38: 0}


print(BlackShoes)

while True:
    purchaseSize = int(
        input(
            "Which shoe size would you like to buy? (Enter any -ve Number to Exit ]:\n"
        )
    )

    # exit the loop with any nagative number 
    if purchaseSize < 0:
        break

    if BlackShoes[purchaseSize] <= 0:
        print(f"Sorry Size {purchaseSize} out of Stock! \n")
    else:
        BlackShoes[purchaseSize] -= 1

    print(BlackShoes)
