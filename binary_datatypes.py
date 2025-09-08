#bytes example
print("Bytes example:")

#creating a byte object
b = bytes([65, 66, 67, 68])
print(b)

#accessing elements in a bytes object
print(b[0])
print(b[1])

#iterating through a bytes object
for byte in b:
    print(byte, end=" ")
print("\n")

#bytearray example
print("Bytearray example:")

#creating a bytearray object
ba = bytearray([65, 66, 67, 68])
print(ba)

#modifying elements in a bytearray
ba[0] = 97
print(ba)

#adding element to bytearray
ba.append(69)
print(ba)

# converting bytearray to bytes
b_converted = bytes(ba)
print(b_converted)
print("\n")

# memoryview example
print("Memoryview example: ")

# creating a bytes object
b_mv = bytes([65, 66, 67, 68, 69])

# creating a memoryview object
mv = memoryview(b_mv)
print(mv[0])

# slicing memoryview
mv_slice = mv[1:4]
print(mv_slice.tobytes())

# creating a bytearray and a memoryview
ba_mv = bytearray([65, 66, 67, 68, 69])
mv_ba = memoryview(ba_mv)

# modifying the original bytearray through memoryview
mv_ba[0] = 97
print(ba_mv)

print("This program is written and executed by Yuvraj Narang")