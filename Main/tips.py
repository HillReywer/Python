bill = float(input("Bill?"))
tip = float(input("Tips?"))
person = int(input("How many people?"))

result = round((((bill /100 * tip) + bill) / person), 2)

print(result)

