weight = float(input("Enter your weight: "))
kg_or_lbs = input("Weight entered above is in Kg or lbs: ")
kilogram = "Kg"
Pound = "lbs"
kg = 2.20462  # lbs
lbs = 0.453592 # kg
if kg_or_lbs == kilogram:
    weight = weight * kg
    print("your weight is " + str(weight) + " lbs")
elif kg_or_lbs == Pound:
    weight = weight * lbs
    print("your weight is " + str(weight)+ " kg")
else:
    print("Please write the correct unit of your weight ")

