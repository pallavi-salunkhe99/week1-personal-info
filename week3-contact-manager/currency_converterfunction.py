# 2. Build a currency converter with multiple conversion functions.

# welcome message
print()
print("*" *90)
print("\t\t\tTo Build a currency converter System")
print("*" *90,"\n")

while True:
    print()
    print("***** Selection Menu *****","\n")
    print("1. INR to USD ")
    print("2. USD to INR")
    print("3. INR to EUR")
    print("4. Exit")
    print()
    
    ch=int(input("Enter your choice: "))
    
    if(ch == 1):
        def inr_to_usd(inr):
            return inr / 83

        inr=float(input("Enter Indian National Rupee: "))
        print("\nUnited States Dollar: ",inr_to_usd(inr),"\n")
    
    elif(ch == 2):
        def usd_to_inr(usd):
            return usd * 83
            
        usd=float(input("Enter United States Dollar: "))
        print("\nIndian National Rupee: ",usd_to_inr(usd),"\n")
    
    elif(ch == 3):
        def inr_to_eur(inr):
            return inr / 90
        
        inr=float(input("Enter Indian National Rupee: "))
        print("\nEuro: ",inr_to_usd(inr),"\n")

    elif(ch == 4):
        break
    
    else:
        print("invalid choice.. please try again.")
        
# good bye message
print()
print("-"*90)
print("\t\t\t\tThanks for visiting my Function CODE.")
print("-"*90,"\n")

