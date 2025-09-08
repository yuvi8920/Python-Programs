# Taking inputs
birth_day, birth_month, birth_year = map(int, input("Enter your birth date (DD/MM/YYYY): ").split("/"))
given_day, given_month, given_year = map(int, input("Enter the given date (DD/MM/YYYY): ").split("/"))

# Initial age calculation
age = given_year - birth_year

# Adjust if birthday hasn't occurred yet in the given year
if (given_month < birth_month) or (given_month == birth_month and given_day < birth_day):
    age -= 1

print(f"Your age on {given_day:02d}/{given_month:02d}/{given_year} will be: {age} years")

print("This program is written and executed by Yuvraj Narang")
