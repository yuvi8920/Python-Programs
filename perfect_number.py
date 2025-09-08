sum = 0
num = int(input("Enter a number: "))
for i in range(1, num):
    if(num % i == 0):
        sum += i

if(sum == num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

print("This program is written and executed by Yuvraj Narang")