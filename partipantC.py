ParticipantNumber = 3

ParticipantData = []

regParticipants = 0 

while (regParticipants < ParticipantNumber):
    temp = []
    name = str(input(f"whats your name?:{regParticipants}\n"))
    temp.append(name)
    country = str(input(f"Country? :{regParticipants}\n"))
    temp.append(country)
    age = str(input(f"How Old are You? :{regParticipants}\n"))
    temp.append(age)
    ParticipantData.append(temp)
    regParticipants += 1

print(ParticipantData) 

for participant in ParticipantData:
    print(participant)   

with open("girls.txt","w") as data:
    for participant in ParticipantData:
        data.write(str(participant))
        data.write("\n")

    