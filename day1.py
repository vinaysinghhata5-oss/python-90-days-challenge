'''
Create a variable name and age, and print them in a sentence like:
👉 My name is Vinay and I am 28 years old.

Write a program that asks for two numbers as input, adds them, and prints the result.

Make a variable is_devops = True and print:
👉 Are you learning DevOps with ? True
'''

name="Vinay"
age=28
print(f"my name is {name} and i am {age} year old")

num1=int(input("Enter firs num:"))
num2=int(input("Enter second num:"))
sum = num1+num2
print(f"sum of two number: {sum}")


is_devops=True
print(f"Are you learning DevOps with ? {is_devops}")


'''
🎯 Extra Challenge (Day 1 Bonus)

Write a program that:

Asks for your name and age as input.

Calculates how old you will be in 5 years.

Prints:
👉 Hello Vinay, in 5 years you will be 33 years old.
'''

name=input("Enter your name:")
age=int(input("Enter your age:"))
total_age=5+age
print(f"Hello {name}, in 5 years you will be {total_age} years old.")