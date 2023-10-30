# a dictionary is a key value pair

# kid = {"name":"irvine","ID":"631400W45","Address":"29 Natal RD"}

# a dictionary by defalt removes repeated elements
# sets are just there to keep track of what you have
# we don't care about the order of elements
# Sets = {"element1", "element2", "element1","element3"}

# if "element1" in Sets:
#     print("Yes")

countryList = []

for country in range(5):
    getCountry = str(input("Enter your motherland : "))
    countryList.append(getCountry)
    
# # set keyword used to convert one data type to a set   
# countrySet = set(countryList)

# # for nyika in countrySet:
# #     print(nyika)

# print(countryList)
# print(countrySet)

# if "Canada" in countrySet:
#     print("Attended")


# dictionaries have a key value pair, there are different from sets in that
# sets only have a one value 

# Dictionary = {"Key":"Value","Key1":"Value2"}

# countyDict = {"Zambeziland":2,"Chinaland":5,"Somalia":0,"Bechuanaland":3}
countyDict = {}

# cool thing about a dictionary is that if an item does not exist it doesnt throw an error, rather it creates the item

for country in countryList:
    if country in countyDict:
        countyDict[country] += 1
    else:
        countyDict[country] = 1

print(countyDict)