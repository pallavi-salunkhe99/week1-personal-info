# 5. Build a simple bank account system with deposit/withdraw functions.


class BackAccount:
    def __init__(self, balance: float = 0.0) ->None:
        self.balance = balance
       
    def to_deposite(self, amount: float) -> None:
        if(amount > 0):
            # deposite amount
            self.balance += amount
            print("\nDeposited amount: ",amount,"\n")
        else:
            print("\nDeposite amount must be positive.\n")
        
    def to_withdraw(self, amount: float) -> None:
        if(amount > 0):
         # withdraw amount
            if (self.balance >= amount):
                self.balance -= amount
                print("\nDeposited amount: ",amount,"\n")
            else:
                print("\nInsufficient funds.","\nCurrent Balance: ",self.balance,"\n")
        else:
            print("\nWithdraw amount must be positive.\n")

    def to_view_balance(self) ->None:
        print("\nCurrent Balance: ",self.balance,"\n")



# welcome message
print()
print("*" *90)
print("\t\t\t\tBank Account System")
print("*" *90,"\n")

def main() -> None:
    account = BackAccount()

    while True:
        print("****** Menu ******\n")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Exit\n")
        
        ch=int(input("Enter Your Choice: "))
        if(ch == 1):
            try:
                amount=float(input("Enter Amount to Deposite: "))
                account.to_deposite(amount)
            except ValueError:
                print("\nInvalid input.. please enter valid number to deposite amount.\n")

        
        elif(ch == 2):
            try:
                amount=float(input("Enter Amount to Withdraw "))
                account.to_withdraw(amount)

            except ValueError:
                print("\nInvalid input.. please enter valid number to deposite amount.\n")
            
        elif(ch == 3):
            account.to_view_balance()
            
        elif(ch == 4):
            break

        else:
            print("\nInvalid Choice.. please try again.\n")
        
        # good bye message
    print()
    print("-"*90)
    print("\t\t\tThanks for visiting my Function CODE.")
    print("-"*90,"\n")
 
if __name__ == "__main__":
    main()

