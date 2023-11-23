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

print(phone_number.get("vaskr")) # get method is safe to use incase there is a typo or keys is not present

print(phone_number["Skidy"])
