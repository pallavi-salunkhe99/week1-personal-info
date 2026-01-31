# Q 1. Create functions for common calculations (area, volume, conversions).

# welcome message
print()
print("*" *90)
print("\t\t\tTo use functions for common calculations")
print("*" *90,"\n")

while True:
    # selection menu 

    print("***** Select option which you want to perform operation *****\n")
    print("1. To Calculate Area")
    print("2. To Calculate Volume")
    print("3. To Unit Conversion")
    print("4. Exit","\n")

    ch=int(input("Enter Your Choice: "))

    if(ch == 1):
       
    #area function
       def cal_area(length, width):
        area=length * width
        return area
       
       length=int(input("Enter Length of Rectangle: "))
       width=int(input("Enter Width of Rectangle: "))
       print()
       print("Area of Rectangle: ",cal_area(length,width)," cm")
       print()

    elif(ch == 2):

    # volume function

        def cal_volume(side):
           return side * side * side
        side=int(input("Enter the side of the Cube: "))
        print()
        print("Volume of Cube: ",cal_volume(side),"cm")
        print()

    elif(ch == 3):
    
    # unit conversion function

        def cm_to_meter(cm):
           return cm / 100
           
        cm = float(input("Enter cm unit to conversion in meter Unit: "))
        print("Meters unit is: ", cm_to_meter(cm))
        print()

    elif(ch == 4):
        break

    else:
        print("Invalid Choice.. please try again.")

# good bye message
print()
print("-"*90)
print("\t\t\t\tThanks for visiting my Function CODE.")
print("-"*90,"\n")

