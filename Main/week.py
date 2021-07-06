age = input("Age?")
age_int = int(age)

now = int(age)

years = 100 - age_int
month = years * 12
weeks = years * 52
days = years * 365

message = f"You have {days} days, {weeks} weeks, and {years} years remaining"
print(message)

print(6 + 4 / 2 - (1 * 2))