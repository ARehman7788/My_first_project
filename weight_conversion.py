weight = float(input("Enter your weight: "))
unit = input("Weight entered is in (K)kg or (L)lbs: ")
kilogram = "K"
Pound = "L"
lbs = 0.453592 # kg
if unit.upper() == kilogram:
    conv_weight = weight / lbs
    conv_unit = "lbs"
    print("your weight is " + str(conv_weight) + conv_unit)  
elif unit.upper() == Pound:
    conv_weight = weight * lbs
    conv_unit = "kg"
    print("your weight is " + str(conv_weight)+ conv_unit)
else:
    print("Please write the correct unit of your weight ")


if conv_unit == "kg" and conv_weight >= 90:
   print("You need to exercise. ")
elif conv_unit == "lbs" and conv_weight >= 198:
    print("You need to exercise. ")
elif conv_unit == "kg" and conv_weight <=57:
    print("Abe maches ki thili. ")
elif conv_unit == "lbs" and conv_weight <=125:
    print("Abe maches ki thili. ")
else:
    print("You are fit bro. ")
