# # File = open("filename","r") # r, w, a, r+
# # File.close()


cities = ["Peth","London","New York", "Tokyo","Joburg"]


vacationFile = open("vacationPlaces.txt","w") #writing mode

for city in cities:
    vacationFile.write(city+"\n")
    
# print("done")

vacationFile.close()

textFile = open("vacationPlaces.txt","r") #reading mode

FstLine = textFile.readline()
print(FstLine)

# ScndLine = textFile.readline()
# print(ScndLine)

# ThrdLine = textFile.readline()
# print(ThrdLine)


for line in textFile:
    print(line,end="")

textFile.close()

# # more cities to append at the end of the file  

africa = ["Harare", "Lusaka", "Gaberone","Windhoek"] 

apendText = open("vacationPlaces.txt","a") # apending more text at the end of the file

for a_city in africa:
    apendText.write(a_city+"\n")

apendText.close()

print("*********************************")


# # readFinal = open("vacationPlaces.txt","r") #reading the file

# # for text in readFinal:
# #     print(text)

# # theWholeFile = openDis.read()

# # print(theWholeFile)

# # vacationFile.close()


file =  open("vacationPlaces.txt","r")

def load(x):
    # for i in x:
    #     print(i,end="")
    
    out = x.read()
    return out

print(load(file))
# load(file)


# with open("vacationPlaces.txt","r") as vacationFile:
#     for line in vacationFile:
#         print(line,end="")