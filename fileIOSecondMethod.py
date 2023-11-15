# another way to open a file, the advantage is that you don't have to remember to close the file

# with open("vacationPlaces.txt","r") as txtfile:
#     for line in txtfile:
#         print(line,end="")


# appending using new method 


asian_cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Dhaka', 'Mexico City', 'Cairo', 'Bangkok', 'Karachi']


with open("holiday.txt","w") as txtfile:
    for city in asian_cities:
        txtfile.write(city+"\n")    

# holiday = open("holiday.txt","r")

# for line in holiday:
#     print(line,end="")

# holiday.close()    


with open("holiday.txt","r") as txtfile:
    for line in txtfile:
        print(line)
    # out = txtfile.read()  
    # print(out)  
    
