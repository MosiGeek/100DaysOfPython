# File = open("filename","r") # r, w, a, r+
# File.close()


cities = ["Peth","London","New York", "Tokyo","Joburg"]


vacationFile = open("vacationPlaces.txt","w")

for city in cities:
    vacationFile.write(city+"\n")
    
print("done")

vacationFile.close()
