length = int(input("Enter the length (whole Number)"))
width = int(input("Enter the width (whole Number)"))
price = float(input("Enter the price per unit (numbers and whole Numbers)"))


#Calculation
total_area = length * width
total_cost = total_area * price

print("$",total_cost)

