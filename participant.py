# # collecting and writing tourist data to an external file 

# touristData = []

# touristCounter = 0
# max = 2


# while touristCounter < max:
#     temp = []
    
#     name = input(f"Name :{str(touristCounter)}\n")
#     temp.append(name)
    
#     dob = input(f"D.O.B :{str(touristCounter)}\n")
#     temp.append(dob)
    
#     nat = input(f"Nationality :{str(touristCounter)}\n")
#     temp.append(nat)
    
#     ppn = input(f"Passport Number :{str(touristCounter)}\n")
#     temp.append(ppn)
    
#     ppExp = input(f"Passport Expiry Date :{str(touristCounter)}\n")
#     temp.append(ppExp)
    
#     occ = input(f"Occupation :{str(touristCounter)}\n")
#     temp.append(occ)
    
#     touristData.append(temp)
#     touristCounter += 1


# with open("tourist.txt","w") as tourist:
#     for tdata in touristData:
#         for data in tdata:
#             tourist.write(data+"\n")
#         tourist.write("\n")    


with open("tourist.txt","r") as data:
    tempdata = data.read()
    print(tempdata)       