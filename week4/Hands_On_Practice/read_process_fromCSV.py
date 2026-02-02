# 3. Read and process data from CSV files.

print()
print("*"*90)
print("\t\t\tRead and process data from CSV files")
print("*"*90,"\n")

import csv
total =0
count =0
with open('student.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  print("----------- Student Data -----------\n\n")
  print("1. Read Data From student.csv files.\n")
  for lines in csvFile:
        print(lines)

print("\n\n2. Process data from CSV file.")
print("\n======  To calculate student marks Avg   ======\n")
with open('student.csv', mode ='r')as file:
    csvFile = csv.reader(file)

    for row in csvFile:
        marks = int(row[3])
        total += marks
        count +=1
avg = total/count
print("Average Marks =", avg)


print()
print("-"*90)
print("\t\t\tThanks for looking my code")
print("*"*90,"\n")