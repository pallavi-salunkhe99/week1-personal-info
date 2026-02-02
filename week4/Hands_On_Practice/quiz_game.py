# 4. Create a quiz game that saves scores to a file.

print()
print("*"*90)
print("\t\t\t\tQuiz Game")
print("*"*90,"\n")

quiz = {
    "What does CPU stand for? " : "Central Processing Unit",
    "Which symbol is used for comments in Python?" : "#",
    "Which data type stores True or False in Python?" : "bool",
    "What function is used to take input from the user in Python?" : "input()",
    "Which keyword is used to create a loop that runs while a condition is true?" : "while"
}

def display_menu():
    print("----------------  Selection Menu  ----------------\n")
    print("1. Start Quiz")
    print("2. View All Questions and Answers")
    print("3. Add a New Question")
    print("4. Delete a Question")
    print("5. Exit\n")

def star_quiz():
    score=0
    i=1

    print("\n==========  Starting Quiz  ==========\n")
    name = input("Enter your Name: ")
    for question, ans in quiz.items():
        print("\nQuestion",i)
        print(question)
        i +=1

        user_ans = input("Enter Your Answer: ").strip()

        if user_ans.lower() == ans.lower():
            print("\nCorrect.!\n")
            score +=1
        else:
            print("\nwrong! correct Answer: ",ans,"\n")
    
    print("\n===========   Quiz Complete   ===========\n")
    print("Name: ",name)
    print("\nYour Score: ",score , "out of ",len(quiz))
    with open("score.txt","a") as f:
        f.write(name +"\t\t\t\t\t"+ str(score) + "\n")
    print()

    print()
    print("*"*90)
    print("\t\t\t Thanks for visiting my quiz game")
    print("*"*90,"\n")

def view_quiz():
    print("\n===========   Quiz Questions & Answers   ===========\n")
    i=1
    for question, ans in quiz.items():
        print("Q ",i,question)
        print("A:",ans,"\n")
        i+=1
    print("="*60,"\n")

def add_new_question():
    question = input("Enter the new Question: ").strip()
    ans = input("Enter the new answer: ").strip()

    if question in quiz:
        print("Question Already Exists!")
    else:
        quiz[question] = ans
        print("Question Added Successfully!")

def delete_quenction():
    question = input("Enter the Question: ").strip()
    if question in quiz:
        del quiz[question]
        print("\nQuestion Deleted Succsufully\n")
    else:
        print("\nQuestion not Found\n")

while True:

    display_menu()
    ch = int(input("Enter your choice: "))

    if(ch == 1):
        star_quiz()

    elif(ch == 2):
        view_quiz()
    
    elif(ch == 3):
        add_new_question()

    elif(ch == 4):
        delete_quenction()
    
    elif(ch == 5):
        break

    else:
        print("\n Invalid choice.. plese try again. \n")

print()
print("*"*90)
print("\t\t\t Thanks for visiting my quiz game")
print("*"*90,"\n")
