# Q 6.Practice different list operations and methods

# To create and display list in python.

print("\n")
print("*"*70)
print("\t\t\tList Operation")
print("*"*70)
print("\n")

print("***** Display List *****\n")
list=[1,2,3,4,5,6]
print(list)
print("")

# list operations
print("***** List Operations *****\n")
print("1. Access:-Access element")
print("Element is: ",list[0])
print("\n2. Slicing:-Sublist")
print("Element is: ",list[0:3])
print("\n3. Length:-Number of elements")
print("Element Length is: ",len(list))
list1=[1,2,3,4,5,6]
list2=[7,8,9,10]
print("\n4. Concatenation:-Join lists")
print("Concatenation list are: ",list1+list2)

# List Methods (Built-in)
print("\n***** List Methods *****\n")
print("1. Adding Elements")
list.append(7)
print("added Element in list is: ",list)

print("\n2. Removing Elements")
print("Element is: ",list.pop())
print("removing Element in list is: ",list)

print("\n3.Rearranging / Modifying")
list.reverse()
print("To reverse Elements in list is: ",list)

print("\n4. Searching / Counting")
list3=[1,2,3,4,5,6,1,1]
print("count 1 number in list is: ",list3.count(1))

print()
print("-"*70)
print("\t\tThanks for visiting me My Python Program..!")
print("-"*70)
print()