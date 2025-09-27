'''
Q1. Print numbers 1–10 using a for loop.
Q2. Print numbers 1–10 using a while loop.
Q3. Sum of first 10 numbers using a for loop.
Q4. Multiplication table for a number entered by user.
'''

for i in range(1,11):
    print(i)

count=1
while count<=10:
    print(count)
    count+=1
y=0
for x in range(1,11):
    y+=x
    print(y)
num=int(input("Enter the number:"))
mul=0
for b in range(1,11):
    mul=num*b
    print(f"{num}*{b} = {mul}")

