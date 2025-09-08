try:
    file = open('example.txt','r')
    content = file.read()
except FileNotFoundError:
    print("Error: This file was not found.")
finally:
    file.close()

print("This program is written and executed by Yuvraj Narang")