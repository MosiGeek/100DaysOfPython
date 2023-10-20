# # loops

# # starting with for loops

# word = "Hello"
# letters = []

# for i in word:
#     print(i)
#     if i == "e":
#         print("What a funny letter")
#     letters.append(i)


# print("**************************************************")
# print(letters)
# print("**************************************************")

# print(letters[1:4])


# numbers = [1,2,3,4,5]
# odd = []
# even = []
# for j in numbers:
#     if j%2 == 0:
#         print(f"{j} is Even")
#         even.append(j)
#     else:
#         print(f"{j} is Odd")
#         odd.append(j)

# print("**************************************")

# print(f"odd {odd}")
# print(f"even {even}")



# using the range function
# range(start,stop-upto but not including,steps/increament)
Numbers = []
for num in range(1,10,2):
    Numbers.append(num)
    print(num) 

print(Numbers)