num = int(input("Enter a number: "))
temp = num
sum_of_powers = 0

num_digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

print("This program is written and executed by Yuvraj Narang")