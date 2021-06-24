height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = (weight / float(height) ** 2)
bmi_less = int(bmi)
print(bmi_less)