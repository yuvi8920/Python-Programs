def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

def squared_number(numbers):
    for number in numbers:
        yield number ** 2
for square in squared_number(count_up_to(5)):
    print(square)

print("This program is written and executed by Yuvraj Narang")