# 6. Practice handling different file-related errors.

# File Not Found Error
try:
    f = open("data1.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: File does not exist.")

# Permission Error

try:
    f = open("data1.txt", "w")
    f.write("Hello")
    f.close()
except PermissionError:
    print("Error: Permission denied.")
