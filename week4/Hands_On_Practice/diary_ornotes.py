# 2. Build a simple diary/notes application with file storage.

print()
print("*"*90)
print("\t\t\t\tDiary/notes Application")
print("*"*90,"\n")

while True:
    print("---------- Menu ----------\n")
    print("1. Add note ")
    print("2. View all notes")
    print("3. Exit\n")

    diary_info ={}
    
    ch= int(input("Enter your choice: "))

    if(ch == 1):
        print("\n\n==========================  Welcome To My Diary Application  ==========================\n\n")
        print("\tFirst give your note a unique title, then write your thoughts or information\n")
        date = input("Enter Date (ex. 01-01-2026): ")
        title = input("Enter Title: ")
        description = input("Enter Your Description Here: ")

        diary_info[title] = {
            "date" : date,
            "description" : description }
        
        import os
        if not os.path.exists("diary.txt") or os.path.getsize("diary.txt")==0:
            with open("diary.txt","w") as f:
              f.write(" Date\t\t\t " + "  Title\t\t\t " + "   Description\n")   
        
        with open("diary.txt","a") as f:
            for title, info in diary_info.items():
                f.write(info["date"] + "\t\t\t" + title + "\t\t\t" + info["description"] + "\n")         
        print("\n note addded succsufully.\n")

    elif(ch == 2):
        try:
            with open("diary.txt", "r") as f:
             print("\n==========================     📖 View All Notes    ==============================\n")
             for line in f:
                print(line.strip())
        except FileNotFoundError:
             print("No diary found. Add notes first.\n")
        print("\n==============================----------------------==============================\n")
        print("\n")

    elif(ch == 3):
        break
    
    else:
        print("Invalid choice.. please try again.")
    

print()
print("*"*90)
print("\t\t\tx-x-x-x   Thanks for looking my code   x-x-x-x")
print("*"*90,"\n")
