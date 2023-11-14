# File = open("filename","r") # r, w, a, r+
# File.close()


cities = ["Peth","London","New York", "Tokyo","Joburg"]


vacationFile = open("vacationPlaces.txt","w") #writing mode

for city in cities:
    vacationFile.write(city+"\n")
    
# print("done")

vacationFile.close()

textFile = open("vacationPlaces.txt","r") #reading mode

for line in textFile:
    print(line,end="")


# theWholeFile = openDis.read()


# print(theWholeFile)

# vacationFile.close()

