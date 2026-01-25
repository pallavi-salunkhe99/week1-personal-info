# while loop
# count=1
# while count<=5:
#     print("hello")
#     count +=1
# print(count) 

# print number 1 to 5
# i=1
# while i<=5:
#     print(i)
#     i+=1
# print("loop ended")

# i=5
# while i>=1:
#     print(i)
#     i-=1
# print("loop ended")

# practice question
# 1. print numbers from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

# 2. print numbers from 100 to 1.
# i=100
# while i>=1:
#     print(i)
#     i-=1

# 3. print the multiplication table of a number n.
# n=int(input("Enter Number to make multiplication table of it: "))
# i=1
# while i<=10:
#     print(n , "*", i , "=", n*i )
#     i+=1

# 4. Print the elements of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]
# list =[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(list):
#     print(list[i])
#     i+=1

# search for a number x in this tuple using loop.
# (1,4,9,16,25,36,49,64,81,100)
# search=int(input("Enter number to search in tuple: "))
# tup=(1,4,9,16,25,36,49,64,81,100)
# i=0
# while i< len(tup):
#     if(tup[i] == search):
#         print("Element found at index: ",i)
#         break
#     else:
#         print("finding..")
#     i+=1

# break and continue 
# i=1
# while i<=5:
#     print(i)
#     if(i == 3):
#         break
#     i+=1
# print("loop ended")

# i=0
# while i<=5:
#     if(i == 3):
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=1
# while i<=10:
#     if(i %2 ==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=1
# while i<=10:
#     if(i %2 !=0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# For loop
# list=[1,2,3,4,5]
# for num in list:
#     print(num)

# alphbets=['a','b','c','d']
# for i in alphbets:
#     print(i)

# tup=(1,2,3,4,5,6)
# for i in tup:
#     print(i)

# str="Pallavi"
# for char in str:
#     print(char)

# str="Pallavi"
# for char in str:
#     print(char)
# else:
#     print("END")

# str="Pallavi"
# for char in str:
#     if(char == 'v'):
#         print("v found")
#         break
#     print(char)
# else:
#     print("END")


# Practice QUESTION 
# 1. print the element of the following list using a loop.
# [1,4,9,16,25,36,49,64,81,100]
# list=[1,4,9,16,25,36,49,64,81,100]
# for i in list:
#     print(i)

# search for a number x in this tuple using loop.
# (1,4,9,16,25,36,49,64,81,100)
# tup=(1,4,9,16,25,36,49,64,81,100)
# n=int(input("To search number: "))
# inx=0
# for i in tup:
#     if(i == n):
#         print("number found at index: ",inx)
#     inx+=1

# range()
# seq=range(5)
# for i in seq:
#     print(i)

# for i in range(10):  #range(stop)
#     print(i)

# for i in range(2,10): #range(start,stop)
#     print(i)

# for i in range(2,10,2): #range(start,stop,step)
#     print(i)

# for i in range(2,100,2): #range(start,stop,step)
#     print(i)

# for i in range(1,100,2): #range(start,stop,step)
#     print(i)

# for i in range(1,11,1): #range(start,stop,step)
#     print("2", "*", i, "=", 2*i)

# Practice QUESTIONS
# using for and range()
# 1. print numbers from 1 to 100.
# for i in range(1,101):
#     print(i)

# 2. print numbers from 100 to 1.
# for i in range(100,0,-1):
#     print(i)

# 3. print the multiplication table of a number n.
# n=int(input("Enter a number: "))
# for i in range(1,11):
#     print(n, "*" , i, "=", n*i)


# pass statement
# for i in range(5):
#     pass
# print("some work..")



# Practice QUESTIONS
# 1. WAP to find the sum of n numbers.(using while)
# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)

# 2. WAP to find the factorial of first n numbers (using for)
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)



    

