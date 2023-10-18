# if condition:
#     Action

# click = True
# like = 1

# if click == True:
#     like += 1
#     click = False

# print(like)

# temp = 14

# themo = 15
# print(themo)

# if temp >= 15:
#     themo += 5

# elif temp <= 15:
#     themo -= 5

# print(themo)

Time = "Night"
Sleepy = False
Pajamas = "Off"


if Time == "Night" and Sleepy == True:
    Pajamas = "On"
elif Time == "Day" or Time == "Morning" and Sleepy == False:
    Pajamas = "Off"

print(f"pajamas {Pajamas}")
