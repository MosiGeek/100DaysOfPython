# dictionary are key value pairs

# since version 3.7 python dictionaries are ordered

# keys are immutable that is once defined you can not change them
# keys are case sensitive
# more readable this way  

phone_number = {
    "Munya": 1234, 
    "Vaskr": 6789, 
    "Skidy": 101112
    }

# another way to define a dictionary 

# phone_number = dict({
#     "Munya": 1234, 
#     "Vaskr": 6789, 
#     "Skidy": 101112
#     })


# phone_number = dict([("Munya":1234),("Radzi":1234),("Muti":1234)])

phone_number["Munya"] = {"work":9999,"office":77777}

phone_number["peater"] = {5656565,2323,0o245,8989}


# one way to access the values in the dictionary  using get method

# print(phone_number.get("vaskr")) # get method is safe to use incase there is a typo or keys is not present

# print(phone_number["Skidy"])

print("*******************************************************************")

# Home Work

# data = {
#     1:'Jenny',
#     2:'Ram',
#     0:'Mohan'
# }

# print(data.get(0))  #output is Mohan


print(phone_number)

# use the del keyword to remove keys and values from a dictionary  
del phone_number["peater"]

print(phone_number)

# pop removes the specified item and return the corresponding value
print(phone_number.pop('Skidy'))

print(phone_number)

print(phone_number.popitem()) #removes the last item and returns its key and value

print(phone_number)


# if you want to access only keys in the dictonary then use the key() method 

print(phone_number.keys())

# likewise if you want to access only the values of the dictionary there is the values() method 

print(phone_number.values())

# items() method will create tuple from the dictionary  

print(phone_number.items())

print(dict(phone_number.items()))

for i in phone_number:
    for j in phone_number[i]:
        print(j,phone_number[i][j])
        
print("############################################################################")

for i in phone_number.items():
    print(i)
    
# copying one dictionary to another dictionary  

phone_num2 = phone_number.copy()



print(phone_num2)

# getting the length of a dictionary 

print(len(phone_num2))    
        
    

phone_number.clear() #this will clear the whole dictionary

print(phone_number)

