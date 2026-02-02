# Pallavi Salunkhe
# Project: Personal Finance Tracker
# Project Description: Build a complete personal finance tracker that allows users to add expenses, categorize them, save data to files, and generate monthly reports. 
#                      This final project combines all concepts from Weeks 1-4 into a practical, real-world application.


from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.expense import Expense
from finance_tracker.file_handler import *
from finance_tracker.reports import *
from finance_tracker.utils import get_month_from_date


print()
print("*"*90)
print("\t\t\tPersonal Finance Tracker System")
print("*"*90,"\n")

def start_app():

    manager = ExpenseManager()
    data = load_expenses()
    manager.load(data)

    while True:
        print("\n************** Menu **************\n")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Search Expenses")
        print("4. Generate Monthly Report")
        print("5. View Category Breakdown")
        print("6. Export Data to CSV")
        print("7. View Statistics")
        print("8. Backup/Restore Data")
        print("9. Exit\n")

        ch = int(input("Enter your choice: "))
        print()
        if ch == 1:
            print("\n\t\t ----------------- Welcome To Personal Finance Tracker System -----------------\n")
            date = input("Enter Date (YYYY-MM-DD): ")
            category = input("Enter Category (ex., food,travel.): ")
            description = input("Enter Description: ")
            amount = float(input("Enter the Amount: "))

            exp = Expense(date, category, description, amount)
            manager.add_expense(exp)
            save_expenses([e.to_dict() for e in manager.get_all_expenses()])
            print("\nExpense added successfully!\n")


            
        elif ch == 2:
            print("\n")
            for e in manager.get_all_expenses():
                print(e.date, e.category, e.description, e.amount)

        
        elif ch == 3:
            cat = input("\nEnter Category: ")
            print()
            results = manager.search_by_category(cat)
            for e in results:
                print(e.date, e.category, e.description, e.amount)
        
        elif ch == 4:
            month = input("Enter month (YYYY-MM): ")
            print("\nTotal: ",monthly_report(manager.get_all_expenses(),month))
            

        elif ch == 5:
            data = category_breakdown(manager.get_all_expenses())
            for k,v in data.items():
                print(k,":",v)
        
        elif ch == 6:
            export_to_csv(manager.get_all_expenses())
            print("\nData exported to CSV successfully!\n")

        elif ch == 7:
            stats = statistics(manager.get_all_expenses())
            print(stats)

        elif ch == 8:
            backup_data()
            print("\n Backup created! \n")

        elif ch == 9:
            break
        
        else:
            print("\n Invalid choice.. plese try again.\n")


    print()
    print("*"*90)
    print("\t\tThanks for using our Personal Finance Tracker System!")
    print("*"*90,"\n")





