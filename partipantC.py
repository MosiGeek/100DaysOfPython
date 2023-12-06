# ParticipantNumber = 3

# ParticipantData = []

# regParticipants = 0 

# while (regParticipants < ParticipantNumber):
#     temp = []
#     name = str(input(f"whats your name?:{regParticipants}\n"))
#     temp.append(name)
#     country = str(input(f"Country? :{regParticipants}\n"))
#     temp.append(country)
#     age = str(input(f"How Old are You? :{regParticipants}\n"))
#     temp.append(age)
#     ParticipantData.append(temp)
#     regParticipants += 1

# print(ParticipantData) 

# for participant in ParticipantData:
#     print(participant)   

# with open("girls.txt","w") as data:
#     for participant in ParticipantData:
#         for row in participant:
#             data.write(str(row))
#             data.write(" ")
#         data.write("\n")


girls = []

with open("girls.txt","r") as file:
    for line in file:
        temp = line.strip(" ").split() 
        girls.append(temp)  

# min = 100
# i = 0
# while i <= 2:
#     # print(girls[i][2])
#     if min > int(girls[i][2]):
#         min = int(girls[i][2])
#     i += 1

# print(min)

print(girls)

for i in girls:
    print(i[2])


        


