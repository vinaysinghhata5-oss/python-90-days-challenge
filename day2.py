'''
Q1. Voting Eligibility

Ask user for age.
👉 If age ≥ 18 → print "You are eligible to vote"
👉 Else → "You are not eligible to vote"
'''
age=int(input("Enter you age:"))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


'''
Q2. Number Sign Checker

Ask user for a number.
👉 Print whether it’s "Positive", "Negative", or "Zero".
'''
num=int(input("Enter any number:"))
if num>0:
    print(f"{num} is positive")
elif num==0:
    print(f"{num} is zero")
else:
    print(f"{num} is negative")


'''
Q3. Even or Odd

Ask user for a number.
👉 Print whether it’s "Even" or "Odd".
'''
num1=int(input("Enter any number:"))
if num1%2==0:
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")


'''
🎯 Day 2 Bonus Challenge

Write a program that asks for marks (0–100) and prints the grade:

90–100 → "Grade: A"

75–89 → "Grade: B"

50–74 → "Grade: C"

<50 → "Grade: Fail"
'''

marks=int(input("Enter the Marks:"))
if marks>=90 and marks<=100:
    print("Grade: A")
elif marks>=75 and marks <=89:
    print("Grade: B")
elif marks >=50 and marks<=74:
    print("Grade: C")
else:
    print("Grade: Fail")