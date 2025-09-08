count = 0 
for year in range(1, 2025):
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print(year)
        count += 1

print(f"Toal years: {count}")

print("This program is written and executed by Yuvraj Narang")