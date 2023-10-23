# breaking and continuing in Loopslear
# alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# for letter in alphabet:
#     print(letter)
    
participants = ["Jen","Shauna","Kyle","Tamy","Vaskr"] 

position = 1

# for name in participants:
    
#     if name == "Tamy":
#         print(position,name)
#         # print("About to break",position)
#         break
#     # print("about to Increament",position)
#     position += 1

name = str(input("Enter name to search here: "))

index = 1
for cur_index in range(len(participants)):
    if participants[cur_index] == name:
        print(f"found {name} at position {index}")
        break
    else:
        print("Not Found")
        
    index += 1    