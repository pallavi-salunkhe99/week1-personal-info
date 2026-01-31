# 4.Make a text analyzer that counts words, characters, and vowels.

# welcome message
print()
print("*" *90)
print("\t\t\t\tText Analyzer System")
print("*" *90,"\n")

while True:
    print("***** Menu *****\n")
    print("1. Count Words")
    print("2. Characters")
    print("3. Vowels")
    print("4. Exit\n")

    def is_text():
        text=input("Enter text: ")
        return text

    ch=int(input("Enter Your Choice: "))
    if(ch == 1):
        text = is_text()
        print("\nTotal Words: ",len(text.split()),"\n")

    elif(ch == 2):
        text = is_text()
        print("\nTotal Characters: ",len(text),"\n")

    elif(ch == 3):
        text=is_text()
        vowel_count=0
        for ch in text.lower():
            if(ch in "aeiou"):
                vowel_count +=1
        print("\nTotal Vowels: ",vowel_count,"\n")
    
    elif(ch == 4):
        break

    else:
        print("Invalid choice.. try again.")
        
# good bye message
print()
print("-"*90)
print("\t\t\tThanks for visiting my Function CODE.")
print("-"*90,"\n")

