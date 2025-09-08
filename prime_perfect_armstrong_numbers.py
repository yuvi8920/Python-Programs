start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("\nPrime numbers:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

print("\n\nPerfect numbers:")
for num in range(start, end + 1):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    if sum_div == num and num != 0:
        print(num, end=" ")

print("\n\nArmstrong numbers:")
for num in range(start, end + 1):
    num_digits = len(str(num))
    sum_of_powers = sum(int(d) ** num_digits for d in str(num))
    if sum_of_powers == num:
        print(num, end=" ")

print("\n")
print("This program is written and executed by Yuvraj Narang")